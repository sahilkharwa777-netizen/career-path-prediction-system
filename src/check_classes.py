import pandas as pd

df = pd.read_csv("data/raw/PS2_Dataset.csv")

print("Unique careers:")
print(df["Suggested Job Role"].unique())

print("\nTotal careers:")
print(df["Suggested Job Role"].nunique())