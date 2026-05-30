import pandas as pd
from sklearn.preprocessing import LabelEncoder

import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "raw", "PS2_Dataset.csv")

df = pd.read_csv(file_path)

yes_no_cols = [
    "self-learning capability?",
    "Extra-courses did",
    "Taken inputs from seniors or elders",
    "worked in teams ever?",
    "Introvert"
]

for col in yes_no_cols:
    df[col] = df[col].astype(str).str.lower()
    df[col] = df[col].map({
        "yes": 1,
        "no": 0
    })

label_encoders = {}

for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

print(df.head())
print(df.info())
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 Rows:")
print(df.head())