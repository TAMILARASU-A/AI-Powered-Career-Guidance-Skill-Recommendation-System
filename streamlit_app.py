import streamlit as st
import plotly.express as px
import pandas as pd
import os
from pyspark_etl import get_insights  # ✅ Keep this if your PySpark script exists

# --- STREAMLIT CONFIG ---
st.set_page_config(layout="wide", page_title="AI Career Guidance System")
st.title("💡 AI-Powered Career Guidance & Skill Recommendation System")
st.markdown("---")

# --- LOAD DATA (Safe Fallback if PySpark Fails) ---
with st.spinner("Running PySpark ETL... Please wait (30–60s on first run) ⏳"):
    try:
        job_demand_data, recommendations_data = get_insights()
        st.success("✅ PySpark ETL completed successfully!")
    except Exception as e:
        st.error(f"⚠️ PySpark failed: {e}")
        # Fallback: Load from saved CSV instead
        if os.path.exists("updated_recommendations.csv"):
            recommendations_data = pd.read_csv("updated_recommendations.csv")
            st.info("Loaded data from local CSV as backup.")
        else:
            recommendations_data = pd.DataFrame(columns=[
                'student_name', 'specialization', 'cgpa_percent',
                'job_title', 'industry', 'cert_course_title', 'avg_salary', 'Skill Match (%)'
            ])
            st.warning("No data found — a new dataset will be created.")
        job_demand_data = pd.DataFrame({
            'industry': ['IT', 'Finance', 'Healthcare'],
            'number_of_jobs': [1200, 800, 500],
            'average_salary': [700000, 600000, 550000]
        })

# --- SIDEBAR CONTROLS ---
st.sidebar.header("🔧 Controls")
view_mode = st.sidebar.radio(
    "Select View Mode:",
    ('Market Insights', 'Personalized Recommendation', 'Skill Recommendation Editor')
)

# ================================================================
# 📊 MARKET INSIGHTS
# ================================================================
if view_mode == 'Market Insights':
    st.header("📊 Job Market Insights")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Industry Demand by Job Volume")
        fig_demand = px.bar(
            job_demand_data,
            x='industry',
            y='number_of_jobs',
            color='average_salary',
            title='Job Volume & Estimated Average Salary by Industry'
        )
        st.plotly_chart(fig_demand, use_container_width=True)

    with col2:
        st.subheader("Top 10 High-Demand Industries")
        st.dataframe(
            job_demand_data.sort_values(by='number_of_jobs', ascending=False).head(10),
            use_container_width=True,
            hide_index=True
        )

# ================================================================
# 🎯 PERSONALIZED RECOMMENDATIONS
# ================================================================
elif view_mode == 'Personalized Recommendation':
    st.header("🎯 Personalized Skill Recommendations")

    if not recommendations_data.empty:
        students = recommendations_data['student_name'].unique().tolist()
        selected_student = st.selectbox("Select Student:", options=students, index=0)
        student_recs = recommendations_data[recommendations_data['student_name'] == selected_student]

        if not student_recs.empty:
            col1, col2 = st.columns([3, 2])

            with col1:
                st.subheader(f"Top Jobs for {selected_student}")
                st.dataframe(
                    student_recs.sort_values(by='Skill Match (%)', ascending=False)
                    .rename(columns={'cgpa_percent': 'CGPA/Percent', 'cert_course_title': 'Certification'}),
                    use_container_width=True,
                    hide_index=True
                )

            with col2:
                st.subheader("Suitability vs. Salary")
                fig = px.scatter(
                    student_recs,
                    x='Skill Match (%)',
                    y='avg_salary',
                    color='industry',
                    hover_data=['job_title'],
                    size='Skill Match (%)',
                    title="Job Suitability & Salary Comparison"
                )
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning(f"No matches found for {selected_student}. Try another student.")
    else:
        st.info("No data available. Please add recommendations first in the editor.")

# ================================================================
# 🛠️ SKILL RECOMMENDATION EDITOR (CRUD)
# ================================================================
elif view_mode == 'Skill Recommendation Editor':
    st.header("🛠️ Skill Recommendation Editor (CRUD)")

    # READ
    st.subheader("1️⃣ Read: View All Recommendations")
    st.dataframe(recommendations_data.head(20), use_container_width=True)

    # CREATE
    st.subheader("2️⃣ Create: Add a New Recommendation")
    with st.form("add_recommendation"):
        new_name = st.text_input("Student Name")
        new_job = st.text_input("Job Title")
        new_industry = st.text_input("Industry")
        new_salary = st.number_input("Salary", min_value=0)
        new_skill_match = st.number_input("Skill Match (%)", min_value=0.0, max_value=100.0)
        submitted = st.form_submit_button("Add Recommendation")

        if submitted:
            if new_name and new_job:
                new_row = pd.DataFrame([{
                    'student_name': new_name,
                    'specialization': 'N/A',
                    'cgpa_percent': 0,
                    'job_title': new_job,
                    'industry': new_industry,
                    'cert_course_title': 'N/A',
                    'avg_salary': new_salary,
                    'Skill Match (%)': new_skill_match
                }])
                recommendations_data = pd.concat([recommendations_data, new_row], ignore_index=True)
                recommendations_data.to_csv("updated_recommendations.csv", index=False)
                st.success(f"✅ Added recommendation for {new_name} → {new_job}")
            else:
                st.warning("⚠️ Please fill both Student Name and Job Title.")

    # UPDATE
    st.subheader("3️⃣ Update: Modify Skill Match of a Recommendation")
    if not recommendations_data.empty:
        rec_to_update = st.selectbox("Select a Recommendation to Update", recommendations_data['student_name'].unique(), key='update_box')
        new_skill = st.number_input("New Skill Match (%)", min_value=0.0, max_value=100.0, key='update_skill')

        if st.button("Update Skill Match"):
            recommendations_data.loc[
                recommendations_data['student_name'] == rec_to_update,
                'Skill Match (%)'
            ] = new_skill
            recommendations_data.to_csv("updated_recommendations.csv", index=False)
            st.success(f"✅ Updated Skill Match for {rec_to_update} to {new_skill}%")
    else:
        st.info("No records available to update.")

    # DELETE
    st.subheader("4️⃣ Delete: Remove a Recommendation")
    if not recommendations_data.empty:
        rec_to_delete = st.selectbox("Select a Recommendation to Delete", recommendations_data['student_name'].unique(), key='delete_box')
        if st.button("Delete Recommendation"):
            recommendations_data = recommendations_data[recommendations_data['student_name'] != rec_to_delete]
            recommendations_data.to_csv("updated_recommendations.csv", index=False)
            st.success(f"🗑️ Deleted all recommendations for {rec_to_delete}")
    else:
        st.info("No records available to delete.")

    st.markdown("✅ **All CRUD changes are now automatically saved to `updated_recommendations.csv`.**")
