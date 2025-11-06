
# 🎯 AI-Powered Career Guidance & Skill Recommendation System

This project helps students find suitable career paths and skill recommendations based on their academic performance and skill set.
It uses **PySpark** for handling large datasets and **Streamlit** for a simple interactive interface.

---

## 🧩 Project Aim

To build an intelligent system that analyzes student data and job-market information to give **personalized career suggestions** and **skill recommendations**.

---

## ⚙️ How It Works

1. **Data Loading** – Loads student and job data using PySpark.
2. **Data Cleaning** – Removes missing values and cleans text.
3. **Skill Tokenization** – Splits skills for students and job posts.
4. **Skill Matching** – Calculates how much a student’s skills match job requirements using Jaccard similarity.
5. **Job Market Analysis** – Finds top industries and average salaries.
6. **Streamlit App** – Shows recommendations, job insights, and allows adding, updating, or deleting recommendations.

---

## 🧠 Technologies Used

| Category      | Tools          |
| ------------- | -------------- |
| Big Data      | PySpark        |
| Web App       | Streamlit      |
| Data Handling | Pandas         |
| Visualization | Plotly Express |
| Language      | Python         |

---

## 🗂️ Project Files

```
career-guidance/
├── app.py                  # Streamlit interface
├── spark_etl.py            # PySpark data processing
├── utils.py                 # Helper functions
├── data/
│   ├── career_recommender.csv
│   ├── all_job_post.csv
│   ├── recommendations.parquet
├── requirements.txt
└── README.md
```

---

## 🧾 Sample Data

**Students (career_recommender.csv)**

| student_name | skills          | cgpa | location |
| ------------ | --------------- | ---- | -------- |
| Aadil        | Python, SQL, ML | 8.2  | Chennai  |

**Jobs (all_job_post.csv)**

| job_title    | skills             | industry    | salary   |
| ------------ | ------------------ | ----------- | -------- |
| Data Analyst | SQL, Python, Excel | IT/Software | 7,00,000 |

---

## 🪄 Setup and Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/TAMILARASU-A/AI-Career-Guidance-System.git
   cd AI-Career-Guidance-System
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run PySpark ETL**

   ```bash
   python spark_etl.py
   ```

4. **Start Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## 🌟 Features

* Load and process large datasets using PySpark
* Personalized job and skill recommendations
* Job market insights (demand, salary, industries)
* CRUD operations (Create, Read, Update, Delete)
* Easy-to-use Streamlit dashboard

---

## 🔮 Future Add-ons

* Machine learning to predict job matches
* NLP for better skill extraction
* Live job data via APIs
* Cloud deployment (AWS / GCP / Azure)
* Interactive dashboards

---

## 💻 Requirements

| Software  | Version |
| --------- | ------- |
| Python    | 3.9+    |
| PySpark   | 3.5+    |
| Streamlit | 1.36+   |
| Pandas    | 2.2+    |
| Plotly    | 5.22+   |
| PyArrow   | 15.0+   |

> ⚠️ Make sure Java (JDK 11+) is installed and `JAVA_HOME` is set.

---

## 👨‍💻 Team Members

### 🧑‍💻 Tamilarasu A 

🎓 MCA Student – Coimbatore Institute of Technology (CIT), Coimbatore
💡 Passionate about AI, Data Engineering & Python-based Big Data Solutions
🔗 [GitHub Profile](https://github.com/TAMILARASU-A)

---

### 👩‍💻 Sridevi R

🎓 MCA Student – Coimbatore Institute of Technology (CIT), Coimbatore
💡 Aspiring Software Engineer | Interested in AI & ML and Data Analytics, Web Development 
🔗 [GitHub Profile](https://github.com/Sridevi2108)

---

## 🏁 Conclusion

This system acts as a **career guide** for students, helping them identify suitable job roles and the right skills to improve, based on real job-market data.

---
