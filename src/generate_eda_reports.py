import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create output directory
output_dir = "reports/screenshots"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/PS2_Dataset.csv")

# ----------------------------
# 1. Career Distribution
# ----------------------------
plt.figure(figsize=(12,6))
df["Suggested Job Role"].value_counts().plot(kind="bar")
plt.title("Career Distribution")
plt.tight_layout()
plt.savefig(f"{output_dir}/career_distribution.png")
plt.close()

# ----------------------------
# 2. Certifications
# ----------------------------
plt.figure(figsize=(10,5))
df["certifications"].value_counts().plot(kind="bar")
plt.title("Certification Distribution")
plt.tight_layout()
plt.savefig(f"{output_dir}/certification_distribution.png")
plt.close()

# ----------------------------
# 3. Workshops
# ----------------------------
plt.figure(figsize=(10,5))
df["workshops"].value_counts().plot(kind="bar")
plt.title("Workshop Distribution")
plt.tight_layout()
plt.savefig(f"{output_dir}/workshop_distribution.png")
plt.close()

# ----------------------------
# 4. Reading Skills
# ----------------------------
plt.figure(figsize=(7,7))
df["reading and writing skills"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Reading & Writing Skills")
plt.savefig(f"{output_dir}/reading_writing_skills.png")
plt.close()

# ----------------------------
# 5. Memory Capability
# ----------------------------
plt.figure(figsize=(7,7))
df["memory capability score"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Memory Capability")
plt.savefig(f"{output_dir}/memory_capability.png")
plt.close()

# ----------------------------
# 6. Correlation Heatmap
# ----------------------------
plt.figure(figsize=(8,6))
sns.heatmap(
    df.select_dtypes(include=["number"]).corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(f"{output_dir}/correlation_heatmap.png")
plt.close()

print("\nAll EDA graphs saved successfully!")
print(f"Location: {output_dir}")