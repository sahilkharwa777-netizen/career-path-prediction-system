# 🎯 Career Path Prediction and Guidance System

## 📌 Overview

The Career Path Prediction and Guidance System is a Machine Learning-based web application designed to help students identify suitable career paths based on their skills, interests, and personal attributes.

The system analyzes various factors such as logical ability, coding skills, communication skills, certifications, workshops attended, learning habits, and career interests to predict the most suitable job role. It also provides recommended courses and learning paths to help users achieve their career goals.

---

## 🚀 Features

* Career Prediction using Machine Learning
* Interactive Streamlit Dashboard
* Personalized Career Recommendations
* Course Recommendation System
* Data Visualization and Analytics
* Feature Importance Analysis
* Confusion Matrix Evaluation
* User-Friendly Interface

---

## 🛠 Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier
* Gradient Boosting Classifier

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Model Storage

* Joblib

### Version Control

* Git
* GitHub

---

## 📂 Dataset Information

The dataset contains information related to:

* Logical Quotient Rating
* Hackathons Participated
* Coding Skills Rating
* Public Speaking Skills
* Certifications
* Workshops Attended
* Reading and Writing Skills
* Memory Capability Score
* Interested Subjects
* Career Interests
* Company Preferences
* Teamwork Experience
* Personality Traits

### Target Variable

**Suggested Job Role**

The dataset contains 12 different career roles including:

* Software Engineer
* Software Developer
* Web Developer
* UX Designer
* Database Developer
* Network Security Engineer
* Systems Security Administrator
* Technical Support
* CRM Technical Developer
* Mobile Applications Developer
* Applications Developer
* Software QA / Testing

---

## 🔄 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Label Encoding
4. Exploratory Data Analysis
5. Model Training
6. Model Evaluation
7. Career Prediction
8. Course Recommendation
9. Dashboard Development
10. Deployment Ready System

---

## 📊 Exploratory Data Analysis

The project includes visualizations such as:

* Career Distribution
* Certification Distribution
* Workshop Distribution
* Reading and Writing Skills Analysis
* Memory Capability Analysis
* Correlation Heatmap
* Feature Importance Analysis
* Confusion Matrix

---

## 🤖 Machine Learning Models

### Random Forest Classifier

Used as the primary prediction model.

### Gradient Boosting Classifier

Used for model comparison.

### Model Performance

| Model             | Accuracy |
| ----------------- | -------- |
| Random Forest     | 8.98%    |
| Gradient Boosting | 7.75%    |

---

## 📚 Course Recommendation System

After predicting a career role, the system recommends relevant courses and skills to help users improve their expertise in the selected domain.

Examples:

* Software Engineering
* Web Development
* Cyber Security
* Database Management
* UI/UX Design
* Networking

---

## 📁 Project Structure

career-path-prediction-system/

├── app/

│ └── streamlit_app.py

├── data/

│ └── raw/

│ └── PS2_Dataset.csv

├── models/

│ ├── feature_encoders.pkl

│ ├── target_encoder.pkl

│ └── label_encoders.pkl

├── notebooks/

│ └── EDA.ipynb

├── reports/

│ └── screenshots/

├── src/

│ ├── train_model.py

│ ├── predict.py

│ ├── model_comparison.py

│ ├── model_evaluation.py

│ ├── generate_eda_reports.py

│ └── course_recommender.py

├── requirements.txt

└── README.md

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/sahilkharwa777-netizen/career-path-prediction-system.git
```

### Move Into Project Folder

```bash
cd career-path-prediction-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

---

## 🎯 Future Improvements

* Deep Learning Integration
* Improved Model Accuracy
* Resume Analysis Feature
* Skill Gap Analysis
* Career Roadmap Generator
* Online Course Integration
* Real-Time Career Recommendations

---

## 👨‍💻 Author

**Sahil Kharwa**

B.Tech Student | Machine Learning Enthusiast | Web Developer

---

## 📜 License

This project is developed for educational and internship purposes.
