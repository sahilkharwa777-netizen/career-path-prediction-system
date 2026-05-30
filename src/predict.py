import joblib
import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load model
model = joblib.load(
    os.path.join(current_dir, "..", "models", "career_model.pkl")
)

# Load target encoder
target_encoder = joblib.load(
    os.path.join(current_dir, "..", "models", "target_encoder.pkl")
)

print("Model Loaded Successfully!")

sample_data = pd.DataFrame({
    "Logical quotient rating": [8],
    "hackathons": [3],
    "coding skills rating": [9],
    "public speaking points": [7],
    "self-learning capability?": [1],
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
    "Management or Technical": [1],
    "hard/smart worker": [1],
    "worked in teams ever?": [1],
    "Introvert": [0]
})

prediction = model.predict(sample_data)

career = target_encoder.inverse_transform(prediction)

print("\nPredicted Career:")
print(career[0])
from course_recommender import recommend_courses

# after career prediction

print("\nPredicted Career:")
print(career[0])

courses = recommend_courses(career[0])

print("\nRecommended Courses:")

for course in courses:
    print("-", course)