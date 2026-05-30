import pandas as pd

df = pd.read_csv("data/raw/PS2_Dataset.csv")

print("Number of careers:")
print(df["Suggested Job Role"].nunique())

print("\nTop 10 careers:")
print(df["Suggested Job Role"].value_counts().head(10))