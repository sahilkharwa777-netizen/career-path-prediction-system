import os
import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load Dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "raw", "PS2_Dataset.csv")

df = pd.read_csv(file_path)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Target column
target_col = "Suggested Job Role"

# Split Features and Target
X = df.drop(columns=[target_col])
y = df[target_col]

# Encode ALL non-numeric columns
feature_encoders = {}

for col in X.columns:

    if not pd.api.types.is_numeric_dtype(X[col]):

        le = LabelEncoder()

        X[col] = le.fit_transform(
            X[col].astype(str)
        )

        feature_encoders[col] = le

# Encode Target
target_encoder = LabelEncoder()

y = target_encoder.fit_transform(
    y.astype(str)
)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Random Forest
model = RandomForestClassifier(
    n_estimators=500,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy * 100:.2f}%")

# Save Model
models_dir = os.path.join(current_dir, "..", "models")

os.makedirs(models_dir, exist_ok=True)

joblib.dump(
    model,
    os.path.join(models_dir, "career_model.pkl")
)

joblib.dump(
    feature_encoders,
    os.path.join(models_dir, "feature_encoders.pkl")
)

joblib.dump(
    target_encoder,
    os.path.join(models_dir, "target_encoder.pkl")
)

print("\nModel Saved Successfully!")