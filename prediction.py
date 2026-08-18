# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 6 - HOUSE PRICE PREDICTION
# ============================================================

import pandas as pd
import joblib


print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 6 : HOUSE PRICE PREDICTION")
print("=" * 70)



# ============================================================
# LOAD MODEL
# ============================================================


model = joblib.load(
    "../models/best_model.pkl"
)


print("\nModel Loaded Successfully")



# ============================================================
# LOAD TEST DATA
# ============================================================


X_test = pd.read_csv(
    "../data/X_test.csv"
)


y_test = pd.read_csv(
    "../data/y_test.csv"
)


y_test = y_test["Price"]



print("\nTest Data Loaded")

print("X_test Shape :", X_test.shape)

print("y_test Shape :", y_test.shape)



# ============================================================
# SELECT ONE HOUSE SAMPLE
# ============================================================


sample_index = 0


sample_house = X_test.iloc[[sample_index]]


actual_price = y_test.iloc[sample_index]



# ============================================================
# PREDICT PRICE
# ============================================================


predicted_price = model.predict(
    sample_house
)[0]



# ============================================================
# DISPLAY HOUSE DETAILS
# ============================================================


print("\nSelected House Features")

print("-" * 70)

print(sample_house)



# ============================================================
# DISPLAY PREDICTION RESULT
# ============================================================


print("\n" + "=" * 70)

print("PREDICTION RESULT")

print("=" * 70)



print(
    f"Actual Price    : ₹ {actual_price:,.2f}"
)


print(
    f"Predicted Price : ₹ {predicted_price:,.2f}"
)



error = abs(
    actual_price - predicted_price
)



print(
    f"Prediction Error: ₹ {error:,.2f}"
)



accuracy = (
    1 - (error / actual_price)
) * 100



print(
    f"Prediction Accuracy : {accuracy:.2f}%"
)



# ============================================================
# SAVE PREDICTION RESULT
# ============================================================


prediction_result = pd.DataFrame({

    "Actual Price":[actual_price],

    "Predicted Price":[predicted_price],

    "Error":[error],

    "Accuracy":[accuracy]

})


prediction_result.to_csv(

    "../data/sample_prediction_result.csv",

    index=False

)



print("\nPrediction Result Saved")



print("\nPrediction Completed Successfully!")

print("=" * 70)

print("STEP 6 COMPLETED SUCCESSFULLY")

print("=" * 70)
