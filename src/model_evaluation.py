import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

# Create output folder
output_dir = "reports/screenshots"
os.makedirs(output_dir, exist_ok=True)

# Load dataset
df = pd.read_csv("data/raw/PS2_Dataset.csv")
df.columns = df.columns.str.strip()

# Split data
X = df.drop("Suggested Job Role", axis=1)
y = df["Suggested Job Role"]

# Encode features
for col in X.columns:
    if not pd.api.types.is_numeric_dtype(X[col]):
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))

# Encode target
target_encoder = LabelEncoder()
y = target_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Load trained model
model = joblib.load("models/career_model.pkl")

# Predictions
y_pred = model.predict(X_test)

# -------------------------
# Confusion Matrix
# -------------------------
plt.figure(figsize=(12,10))
ConfusionMatrixDisplay.from_predictions(
    y_test,
    y_pred
)
plt.title("Confusion Matrix")
plt.savefig(f"{output_dir}/confusion_matrix.png")
plt.close()

# -------------------------
# Feature Importance
# -------------------------
importance = model.feature_importances_

feature_imp = pd.DataFrame({
    "Feature": X.columns,
    "Importance": importance
})

feature_imp = feature_imp.sort_values(
    by="Importance",
    ascending=False
)

plt.figure(figsize=(10,6))
plt.barh(
    feature_imp["Feature"][:10],
    feature_imp["Importance"][:10]
)

plt.title("Top 10 Important Features")
plt.tight_layout()

plt.savefig(
    f"{output_dir}/feature_importance.png"
)

plt.close()

print("\nEvaluation graphs saved successfully!")