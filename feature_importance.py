# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 5 - FEATURE IMPORTANCE ANALYSIS
# ============================================================

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os


print("="*70)
print("STEP 5 : FEATURE IMPORTANCE ANALYSIS")
print("="*70)



# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load(
    "models/best_model.pkl"
)


print("\nModel Loaded Successfully")



# ============================================================
# LOAD FEATURE DATA
# ============================================================

X_train = pd.read_csv(
    "data/X_train.csv"
)


feature_names = X_train.columns



# ============================================================
# EXTRACT FEATURE IMPORTANCE
# ============================================================

if hasattr(model, "feature_importances_"):

    importance = model.feature_importances_


elif hasattr(model, "named_steps"):

    rf_model = model.named_steps[
        list(model.named_steps.keys())[-1]
    ]

    importance = rf_model.feature_importances_


else:

    print("Feature importance not available")
    exit()



# ============================================================
# CREATE DATAFRAME
# ============================================================

feature_df = pd.DataFrame({

    "Feature": feature_names,

    "Importance": importance

})


feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
)



print("\nFEATURE IMPORTANCE TABLE")

print("="*70)

print(feature_df)



# ============================================================
# TOP 10 FEATURES
# ============================================================

top10 = feature_df.head(10)


print("\nTOP 10 IMPORTANT FEATURES")

print("="*70)

print(top10)



# ============================================================
# SAVE RESULTS
# ============================================================

os.makedirs(
    "data",
    exist_ok=True
)


feature_df.to_csv(
    "data/feature_importance.csv",
    index=False
)


print("\nFeature Importance Saved")



# ============================================================
# VISUALIZATION
# ============================================================

plt.figure(
    figsize=(10,6)
)


plt.bar(
    top10["Feature"],
    top10["Importance"]
)


plt.xticks(
    rotation=45,
    ha="right"
)


plt.xlabel(
    "Features"
)


plt.ylabel(
    "Importance Score"
)


plt.title(
    "Random Forest Feature Importance"
)


plt.grid(
    axis="y"
)


plt.tight_layout()


plt.show()



# ============================================================
# FINAL STATUS
# ============================================================

print("\n"+"="*70)

print("STEP 5 COMPLETED")

print("="*70)

print("✓ Feature Importance Calculated")

print("✓ Top Features Identified")

print("✓ Graph Generated")

print("="*70)
