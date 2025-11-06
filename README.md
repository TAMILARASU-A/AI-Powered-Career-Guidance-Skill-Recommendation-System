**🎯 AI-Powered Career Guidance & Skill Recommendation System**

An intelligent big-data application that analyzes student skills, academic performance, and job-market data to provide personalized career guidance and skill recommendations, powered by PySpark, Streamlit, and Plotly.

**📘 Overview**

This project leverages Big Data Processing with PySpark to analyze student skill profiles and job postings at scale.
It matches students with relevant job roles using Jaccard similarity and visualizes job-market trends such as industry demand and average salary.

A Streamlit dashboard enables students and administrators to interactively explore recommendations, manage data via CRUD operations, and gain actionable insights for career planning.

**🚀 Key Features**

✅ Data Processing with PySpark – Load, clean, and transform large CSV datasets.
✅ ETL Pipeline – Extract, Transform, and Load (ETL) with schema inference and tokenization.
✅ Skill-Matching Engine – Uses Jaccard similarity to compute skill-match percentage.
✅ CRUD Operations – Create, Read, Update, Delete recommendations directly from the UI.
✅ Job-Market Insights – Analyze top industries, job demand, and salary distributions.
✅ Interactive Streamlit Dashboard – View recommendations, insights, and manage data visually.
✅ Scalable & Future-Ready – Ready for ML, NLP, and API-integration extensions.

**🧠 System Workflow**

**1️⃣ Data Loading**

Load career_recommender.csv (students) and all_job_post.csv (jobs).

Infer schema automatically and handle multi-line CSVs.

**2️⃣ Data Cleaning & Tokenization**

Remove null/missing values.

Tokenize and normalize skills using PySpark UDF.

**3️⃣ Skill Matching**

Perform cross-join between students and jobs.

Compute skill-match percentage using Jaccard similarity:

Skill Match (%)=∣𝑆𝑘𝑖𝑙𝑙𝑠𝑠𝑡𝑢𝑑𝑒𝑛𝑡∩𝑆𝑘𝑖𝑙𝑙𝑠𝑗𝑜𝑏 ∣
 ∣𝑆𝑘𝑖𝑙𝑙𝑠𝑠𝑡𝑢𝑑𝑒𝑛𝑡∪𝑆𝑘𝑖𝑙𝑙𝑠𝑗𝑜𝑏 ∣ ×100 

**4️⃣ CRUD Operations**

Create → Add new recommendation

Read → View data and insights

Update → Modify match percentage

Delete → Remove recommendation

**5️⃣ Visualization**

Job-market insights using Plotly Express bar charts.

Top 10 industries and skill-based recommendations.

**6️⃣ Streamlit Dashboard**

View, manage, and interact with recommendations in a modern UI.


**🧩 Tech Stack**
Category	Tools / Libraries	Purpose
Big Data Processing	PySpark	ETL, transformations, analytics
Web Framework	Streamlit	User interface & CRUD management
Visualization	Plotly Express	Charts and job-market insights
Data Manipulation	Pandas	Convert Spark DataFrames for UI
Python Core	re, os	String cleaning & environment setup

**📂 Project Structure**
career-guidance/
│
├── app.py                   # Streamlit dashboard
├── spark_etl.py             # PySpark ETL + similarity computation
├── utils.py                 # Skill tokenizer helper
├── data/
│   ├── career_recommender.csv
│   ├── all_job_post.csv
│   ├── recommendations.parquet
│
├── requirements.txt         # Dependencies
└── README.md                # Project documentation






**⚙️ Installation & Setup**
**1️⃣ Clone this repository**
git clone https://github.com/<your-username>/AI-Career-Guidance-System.git
cd AI-Career-Guidance-System

**2️⃣ Create and activate a virtual environment**
python -m venv .venv
source .venv/bin/activate    # (Windows: .venv\Scripts\activate)

**3️⃣ Install dependencies**
pip install -r requirements.txt

**4️⃣ Run PySpark ETL**
python spark_etl.py

**5️⃣ Launch the Streamlit Dashboard**
streamlit run app.py



**📊 Dashboard Preview**

**1️⃣ Job-Market Insights**

Displays industry-wise job demand and average salary using interactive bar charts.

**2️⃣ Personalized Recommendations**

Select a student → view top job matches ranked by skill-match %.

**3️⃣ Manage Recommendations (CRUD)**

Add, update, or delete student-job matches directly.

**🔮 Future Enhancements**

🤖 Machine Learning: Predict best-fit roles and expected salaries.

🧾 NLP: Extract skills from free-text student profiles or resumes.

🌐 API Integration: Fetch live job data from LinkedIn, Indeed, etc.

☁️ Cloud Deployment: Deploy on AWS / GCP / Azure for scalability.

📈 Advanced Dashboards: Use Streamlit or Plotly Dash for deeper insights.



**💻 Requirements**
Dependency	Version
Python	3.9+
PySpark	≥ 3.5.0
Streamlit	≥ 1.36.0
Pandas	≥ 2.2.0
Plotly	≥ 5.22.0
PyArrow	≥ 15.0.0

⚠️ Ensure JDK (Java 11+) is installed and JAVA_HOME is properly configured.

👨‍💻 Authors
🧑‍💻 Tamilarasu A 

🎓 MCA Student – Coimbatore Institute of Technology (CIT), Coimbatore

Email: arasu9725@gmail.com

🔗 GitHub Profile:

👩‍💻 Sridevi R 

🎓 MCA Student – Coimbatore Institute of Technology (CIT), Coimbatore

Email:	Sridevi21082003@gmail.com
🔗 GitHub Profile: Sridevi2108


🏁 Conclusion

The AI-Powered Career Guidance & Skill Recommendation System acts as a smart bridge between students and the job market, helping learners identify the most relevant opportunities and skills to focus on for a successful career path.
