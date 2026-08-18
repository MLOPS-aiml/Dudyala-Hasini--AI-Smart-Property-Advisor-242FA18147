# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 2 : FEATURE ENGINEERING + TRAIN TEST SPLIT
# ============================================================

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 2 : FEATURE ENGINEERING + TRAIN TEST SPLIT")
print("=" * 70)

# ============================================================
# LOAD DATASET
# ============================================================

dataset_path = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data\processed_property_data_New.csv"

df = pd.read_csv(dataset_path)

print("\nDataset Loaded Successfully")
print("Rows    :", df.shape[0])
print("Columns :", df.shape[1])

# ============================================================
# FEATURE ENGINEERING
# ============================================================

print("\nPerforming Feature Engineering...")

# House Size Category
df["HouseSizeCategory"] = pd.cut(
    df["SquareFeet"],
    bins=[0, 1000, 2000, 3500, float("inf")],
    labels=["Small", "Medium", "Large", "Luxury"]
)

# Family Suitability Score
df["FamilySuitabilityScore"] = (
    df["Bedrooms"] * 3 +
    df["Bathrooms"] * 2 +
    df["ParkingSpaces"] * 2 +
    df["Garden"] * 2
)

# Bedroom Density
df["BedroomDensity"] = (
    df["Bedrooms"] / df["SquareFeet"]
).round(4)

# Bathroom Density
df["BathroomDensity"] = (
    df["Bathrooms"] / df["SquareFeet"]
).round(4)

# Age Category
df["AgeCategory"] = pd.cut(
    df["HouseAge"],
    bins=[0, 10, 25, 50, 100],
    labels=["New", "Recent", "Old", "VeryOld"]
)

print("Feature Engineering Completed Successfully")

# ============================================================
# CHECK MISSING VALUES
# ============================================================

print("\nMissing Values")
print(df.isnull().sum())

# ============================================================
# LABEL ENCODING
# ============================================================

print("\nEncoding Categorical Columns...")

categorical_columns = df.select_dtypes(
    include=["object", "category"]
).columns

label_encoders = {}

for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(
        df[column].astype(str)
    )

    label_encoders[column] = encoder

print("Categorical Encoding Completed")

# ============================================================
# FEATURES AND TARGET
# ============================================================

X = df.drop("Price", axis=1)
y = df["Price"]

print("\nFeature Matrix Shape :", X.shape)
print("Target Shape         :", y.shape)

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Data Shape")
print(X_train.shape)

print("\nTesting Data Shape")
print(X_test.shape)

# ============================================================
# SAVE TRAIN TEST DATA
# ============================================================

output_folder = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data"

os.makedirs(output_folder, exist_ok=True)

X_train.to_csv(
    os.path.join(output_folder, "X_train.csv"),
    index=False
)

X_test.to_csv(
    os.path.join(output_folder, "X_test.csv"),
    index=False
)

y_train.to_csv(
    os.path.join(output_folder, "y_train.csv"),
    index=False
)

y_test.to_csv(
    os.path.join(output_folder, "y_test.csv"),
    index=False
)

print("\nTrain-Test Data Saved Successfully")

print("✓ X_train.csv")
print("✓ X_test.csv")
print("✓ y_train.csv")
print("✓ y_test.csv")

print("\nSaved Location:")
print(output_folder)

print("\n" + "=" * 70)
print("STEP 2 COMPLETED SUCCESSFULLY")
print("=" * 70)
