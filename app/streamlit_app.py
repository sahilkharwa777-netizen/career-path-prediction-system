import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Career Path Prediction System",
    page_icon="🎯",
    layout="wide"
)

# ==========================
# LOAD FILES
# ==========================

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(
    BASE_DIR / "models" / "career_model.pkl"
)

target_encoder = joblib.load(
    BASE_DIR / "models" / "target_encoder.pkl"
)

# ==========================
# COURSE RECOMMENDATIONS
# ==========================

career_courses = {

    "Applications Developer": [
        "Python",
        "Java",
        "Software Development",
        "Database Management"
    ],

    "CRM Technical Developer": [
        "Salesforce",
        "CRM Development",
        "SQL",
        "Business Applications"
    ],

    "Database Developer": [
        "SQL",
        "MySQL",
        "MongoDB",
        "Database Design"
    ],

    "Mobile Applications Developer": [
        "Flutter",
        "Android Development",
        "Java",
        "Kotlin"
    ],

    "Network Security Engineer": [
        "Cyber Security",
        "CCNA",
        "Ethical Hacking",
        "Penetration Testing"
    ],

    "Software Developer": [
        "Python",
        "DSA",
        "OOP",
        "Git & GitHub"
    ],

    "Software Engineer": [
        "Python",
        "Data Structures",
        "Algorithms",
        "System Design"
    ],

    "Software Quality Assurance (QA) / Testing": [
        "Manual Testing",
        "Selenium",
        "Automation Testing",
        "Test Cases"
    ],

    "Systems Security Administrator": [
        "Linux",
        "Networking",
        "Cyber Security",
        "CCNA"
    ],

    "Technical Support": [
        "Networking Basics",
        "Linux",
        "System Administration",
        "Customer Support"
    ],

    "UX Designer": [
        "Figma",
        "UI/UX Design",
        "Wireframing",
        "User Research"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js"
    ]
}

# ==========================
# CAREER ROADMAP
# ==========================

career_roadmap = {

    "Software Engineer": [
        "Learn Python",
        "Master DSA",
        "Build Projects",
        "Prepare for Interviews"
    ],

    "Web Developer": [
        "Learn HTML/CSS",
        "Learn JavaScript",
        "Learn React",
        "Build Full Stack Projects"
    ],

    "Systems Security Administrator": [
        "Learn Linux",
        "Study Networking",
        "Learn Cyber Security",
        "Get CCNA Certified"
    ]
}

# ==========================
# SIDEBAR
# ==========================

st.sidebar.title("🎯 Career Guidance System")

st.sidebar.markdown("---")

st.sidebar.metric(
    "Model Accuracy",
    "8.98%"
)

st.sidebar.metric(
    "Career Roles",
    "12"
)

st.sidebar.markdown("---")

st.sidebar.subheader("Technologies")

st.sidebar.write("""
✅ Python

✅ Streamlit

✅ Scikit-Learn

✅ Pandas

✅ Machine Learning
""")

# ==========================
# TITLE
# ==========================

st.title("🎯 Career Path Prediction & Guidance System")

st.markdown(
    "Predict suitable career paths based on skills, interests and academic attributes."
)

st.markdown("---")

# ==========================
# INPUTS
# ==========================

col1, col2 = st.columns(2)

with col1:

    logical = st.slider(
        "Logical Quotient Rating",
        1, 10, 5
    )

    hackathons = st.slider(
        "Hackathons Participated",
        0, 10, 0
    )

    coding = st.slider(
        "Coding Skills Rating",
        1, 10, 5
    )

    speaking = st.slider(
        "Public Speaking Points",
        1, 10, 5
    )

with col2:

    self_learning = st.selectbox(
        "Self Learning Capability",
        ["yes", "no"]
    )

    teamwork = st.selectbox(
        "Worked in Teams",
        ["yes", "no"]
    )

    introvert = st.selectbox(
        "Introvert",
        ["yes", "no"]
    )

    management = st.selectbox(
        "Management or Technical",
        ["Management", "Technical"]
    )

# ==========================
# PREDICTION
# ==========================

if st.button("🚀 Predict Career"):

    sample_data = pd.DataFrame({

        "Logical quotient rating": [logical],
        "hackathons": [hackathons],
        "coding skills rating": [coding],
        "public speaking points": [speaking],

        "self-learning capability?": [
            1 if self_learning == "yes" else 0
        ],

        "Extra-courses did": [1],
        "certifications": [2],
        "workshops": [3],
        "reading and writing skills": [1],
        "memory capability score": [2],
        "Interested subjects": [4],
        "interested career area": [1],
        "Type of company want to settle in?": [3],

        "Taken inputs from seniors or elders": [1],

        "Interested Type of Books": [2],

        "Management or Technical": [
            1 if management == "Technical" else 0
        ],

        "hard/smart worker": [1],

        "worked in teams ever?": [
            1 if teamwork == "yes" else 0
        ],

        "Introvert": [
            1 if introvert == "yes" else 0
        ]
    })

    prediction = model.predict(sample_data)

    career = target_encoder.inverse_transform(
        prediction
    )[0]

    st.markdown("## 🎯 Predicted Career")

    st.success(career)

    st.markdown("## 📚 Recommended Courses")

    courses = career_courses.get(
        career,
        ["No recommendations available"]
    )

    for course in courses:
        st.write(f"✅ {course}")

    st.markdown("## 🛣 Career Roadmap")

    roadmap = career_roadmap.get(career, [])

    if roadmap:
        for step in roadmap:
            st.write(f"➡️ {step}")
    else:
        st.info(
            "Roadmap will be added in future versions."
        )

# ==========================
# PROJECT ANALYTICS
# ==========================

st.markdown("---")
st.header("📊 Project Analytics")

col1, col2 = st.columns(2)

with col1:

    st.image(
        BASE_DIR /
        "reports/screenshots/career_distribution.png",
        caption="Career Distribution"
    )

    st.image(
        BASE_DIR /
        "reports/screenshots/feature_importance.png",
        caption="Feature Importance"
    )

with col2:

    st.image(
        BASE_DIR /
        "reports/screenshots/workshop_distribution.png",
        caption="Workshop Distribution"
    )

    st.image(
        BASE_DIR /
        "reports/screenshots/confusion_matrix.png",
        caption="Confusion Matrix"
    )

# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(
    """
    ### Developed By
    
    Career Path Prediction and Guidance System
    
    Machine Learning Internship Project
    """
)