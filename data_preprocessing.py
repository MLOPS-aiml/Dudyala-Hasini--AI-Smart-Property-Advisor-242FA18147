# ==========================================================
# AI SMART PROPERTY ADVISOR
# STEP 1 - DATA PREPROCESSING
# ==========================================================

import pandas as pd
from sklearn.preprocessing import LabelEncoder


print("="*70)
print("AI SMART PROPERTY ADVISOR")
print("DATA PREPROCESSING")
print("="*70)


# ----------------------------------------------------------
# LOAD DATASET
# ----------------------------------------------------------

df = pd.read_csv(
    "../data/Enhanced_Smart_House_Price_Dataset.csv"
)


print("\nDataset Loaded Successfully")

print("Rows :", df.shape[0])
print("Columns :", df.shape[1])


# ----------------------------------------------------------
# FEATURE ENGINEERING
# ----------------------------------------------------------

CURRENT_YEAR = 2026


# Calculate House Age

df["HouseAge"] = CURRENT_YEAR - df["YearBuilt"]


# House Size Category

df["HouseSizeCategory"] = pd.cut(
    df["SquareFeet"],
    bins=[
        0,
        1000,
        2000,
        3500,
        float("inf")
    ],
    labels=[
        "Small",
        "Medium",
        "Large",
        "Luxury"
    ]
)


# Family Suitability Score

df["FamilySuitabilityScore"] = (
    df["Bedrooms"] * 3 +
    df["Bathrooms"] * 2
)


print("\nFeature Engineering Completed")


# ----------------------------------------------------------
# REMOVE DATA LEAKAGE FEATURES
# ----------------------------------------------------------

remove_columns = [
    "PriceCategory",
    "PricePerSqFt",
    "InvestmentScore",
    "ValueForMoneyScore",
    "NeighborhoodAveragePrice"
]


for column in remove_columns:

    if column in df.columns:
        df.drop(
            column,
            axis=1,
            inplace=True
        )


print("Unwanted Features Removed")


# ----------------------------------------------------------
# ENCODE CATEGORICAL DATA
# ----------------------------------------------------------

categorical_columns = df.select_dtypes(
    include=["object","category"]
).columns


for column in categorical_columns:

    encoder = LabelEncoder()

    df[column] = encoder.fit_transform(
        df[column].astype(str)
    )


print("Label Encoding Completed")


# ----------------------------------------------------------
# SAVE PROCESSED DATA
# ----------------------------------------------------------

df.to_csv(
    "../data/processed_property_data.csv",
    index=False
)


print("\nProcessed Dataset Saved Successfully")


print("="*70)
print("STEP 1 COMPLETED")
print("="*70)