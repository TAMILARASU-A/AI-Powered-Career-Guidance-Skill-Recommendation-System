from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, mean, udf
from pyspark.sql.types import DoubleType, ArrayType, StringType
import pandas as pd
import re
import os
import streamlit as st

# ================================================================
# ENVIRONMENT SETUP (Fix for Python path issue)
python_directory = r"C:\Users\Sakthiswari\AppData\Local\Programs\Python\Python38"
os.environ['PYSPARK_PYTHON'] = os.path.join(python_directory, 'python.exe')
# ================================================================

# --- 1. SPARK INITIALIZATION ---
def init_spark():
    spark = SparkSession.builder \
        .appName("CareerGuidanceETL") \
        .config("spark.driver.memory", "2g") \
        .config("spark.executor.memory", "1g") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark

# --- 2. CLEANING & TOKENIZATION UDF ---
def clean_and_tokenize_skills(skills_str):
    if not skills_str:
        return []
    skills_str = re.sub(r'[\[\]\"\'\(\)]', '', skills_str).lower().strip()
    skills_list = re.split(r'[;,|\s]+', skills_str)
    cleaned = [s.strip() for s in skills_list if len(s.strip()) > 2]
    return cleaned

clean_skills_udf = udf(clean_and_tokenize_skills, ArrayType(StringType()))

# --- 3. MAIN ETL FUNCTION ---
def run_etl(spark):
    """Extract, transform, and load career data."""

    # === READ (R in CRUD) ===
    student_df = spark.read.csv("career_recommender.csv", header=True, inferSchema=True, multiLine=True, escape='"')
    job_df = spark.read.csv("all_job_post.csv", header=True, inferSchema=True, multiLine=True, escape='"')

    # === UPDATE (U in CRUD) ===
    student_df = student_df.withColumnRenamed("What is your name?", "student_name") \
        .withColumnRenamed("What are your skills ? (Select multiple if necessary)", "student_raw_skills") \
        .withColumnRenamed("What is your UG specialization? Major Subject (Eg; Mathematics)", "specialization") \
        .withColumnRenamed("What was the average CGPA or Percentage obtained in under graduation?", "cgpa_percent") \
        .withColumnRenamed("If yes, please specify your certificate course title.", "cert_course_title") \
        .withColumnRenamed("Did you do any certification courses additionally?", "has_certificate")

    job_df = job_df.withColumnRenamed("job_skill_set", "job_raw_skills") \
        .withColumnRenamed("category", "industry")

    # === DELETE (D in CRUD) ===
    student_df = student_df.dropna(subset=['student_raw_skills', 'cgpa_percent'])
    job_df = job_df.dropna(subset=['job_raw_skills'])

    # === CREATE (C in CRUD) ===
    student_df = student_df.withColumn("student_skills", clean_skills_udf(col("student_raw_skills")))
    job_df = job_df.withColumn("job_required_skills", clean_skills_udf(col("job_raw_skills")))
    job_df = job_df.withColumn("avg_salary", (col("job_id") % 50000 + 50000) * 2)

    student_final_df = student_df.select("student_name", "specialization", "cgpa_percent",
                                         "cert_course_title", "student_skills")
    job_final_df = job_df.select("job_title", "industry", "avg_salary", "job_required_skills")

    # === AGGREGATION / READ ===
    job_demand_df = job_final_df.groupBy("industry").agg(
        count("job_title").alias("number_of_jobs"),
        mean("avg_salary").alias("average_salary")
    ).orderBy(col("number_of_jobs").desc())

    # === CROSS JOIN / CREATE ===
    student_final_df = student_final_df.limit(100)
    job_final_df = job_final_df.limit(200)
    combined_df = student_final_df.crossJoin(job_final_df)

    def calculate_match_score(student_skills, required_skills):
        s_set = set(student_skills)
        r_set = set(required_skills)
        if not s_set or not r_set:
            return 0.0
        intersection = len(s_set.intersection(r_set))
        union = len(s_set.union(r_set))
        return (intersection / union) * 100

    match_udf = udf(calculate_match_score, DoubleType())
    recommendation_df = combined_df.withColumn("Skill Match (%)",
                                               match_udf(col("student_skills"), col("job_required_skills")))

    final_recommendation_df = recommendation_df.filter(col("Skill Match (%)") >= 5) \
        .select("student_name", "specialization", "cgpa_percent", "job_title", "industry",
                "cert_course_title", col("avg_salary").cast("integer"), "Skill Match (%)")

    return job_demand_df, final_recommendation_df

# --- 4. CACHED WRAPPER FUNCTION ---
@st.cache_resource(show_spinner=False)
def get_insights():
    """Run ETL once and return Pandas DataFrames."""
    spark = init_spark()
    job_demand_df, final_recommendation_df = run_etl(spark)
    job_demand_pd = job_demand_df.toPandas()
    recommendation_pd = final_recommendation_df.toPandas()
    spark.stop()
    return job_demand_pd, recommendation_pd
