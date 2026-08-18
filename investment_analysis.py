# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 8 - INVESTMENT ANALYSIS
# ============================================================

import os
import pandas as pd
import joblib


print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 8 : INVESTMENT ANALYSIS")
print("=" * 70)



# ============================================================
# PATHS
# ============================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "best_model.pkl"
)


X_TEST_PATH = os.path.join(
    BASE_DIR,
    "data",
    "X_test.csv"
)


Y_TEST_PATH = os.path.join(
    BASE_DIR,
    "data",
    "y_test.csv"
)



# ============================================================
# LOAD MODEL
# ============================================================


model = joblib.load(
    MODEL_PATH
)


print("\nModel Loaded Successfully")



# ============================================================
# LOAD TEST DATA
# ============================================================


X_test = pd.read_csv(
    X_TEST_PATH
)


y_test = pd.read_csv(
    Y_TEST_PATH
)


print("Test Data Loaded Successfully")



# ============================================================
# SELECT PROPERTY
# ============================================================


sample_index = 0


sample_house = X_test.iloc[
    [sample_index]
]


actual_price = y_test.iloc[
    sample_index
]["Price"]



# ============================================================
# PRICE PREDICTION
# ============================================================


predicted_price = model.predict(
    sample_house
)[0]



# ============================================================
# INVESTMENT ANALYSIS
# ============================================================


average_market_price = y_test["Price"].mean()



investment_score = min(

    (average_market_price / predicted_price) * 100,

    100

)



price_difference = (

    average_market_price -

    predicted_price

)



savings_percentage = (

    price_difference /

    average_market_price

) * 100



if predicted_price < average_market_price * 0.80:

    recommendation = "Excellent Investment"


elif predicted_price < average_market_price:

    recommendation = "Good Investment"


elif predicted_price <= average_market_price * 1.20:

    recommendation = "Average Investment"


else:

    recommendation = "Expensive Property"



# ============================================================
# DISPLAY RESULTS
# ============================================================


print("\n" + "=" * 70)

print("INVESTMENT ANALYSIS RESULT")

print("=" * 70)



print(
    f"Average Market Price : ₹ {average_market_price:,.2f}"
)


print(
    f"Actual Price         : ₹ {actual_price:,.2f}"
)


print(
    f"Predicted Price      : ₹ {predicted_price:,.2f}"
)


print(
    f"Investment Score     : {investment_score:.2f}/100"
)


print(
    f"Potential Savings    : {savings_percentage:.2f}%"
)


print(
    f"Recommendation       : {recommendation}"
)



# ============================================================
# SAVE RESULT
# ============================================================


investment_result = pd.DataFrame({

    "Average Market Price":[average_market_price],

    "Actual Price":[actual_price],

    "Predicted Price":[predicted_price],

    "Investment Score":[investment_score],

    "Savings Percentage":[savings_percentage],

    "Recommendation":[recommendation]

})


investment_result.to_csv(

    os.path.join(
        BASE_DIR,
        "data",
        "investment_analysis.csv"
    ),

    index=False

)



print("\nInvestment Analysis Saved")

print(
    "File : data/investment_analysis.csv"
)



print("\nInvestment Analysis Completed Successfully!")

print("=" * 70)

print("STEP 8 COMPLETED SUCCESSFULLY")

print("=" * 70)
