# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 3 : MODEL TRAINING
# ============================================================

import pandas as pd
import numpy as np
import os
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.ensemble import (
    RandomForestRegressor,
    GradientBoostingRegressor,
    ExtraTreesRegressor
)

from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    mean_squared_error
)


print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 3 : MODEL TRAINING")
print("=" * 70)


# ============================================================
# LOAD TRAIN TEST DATA
# ============================================================

data_path = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data"


X_train = pd.read_csv(
    os.path.join(data_path, "X_train.csv")
)

X_test = pd.read_csv(
    os.path.join(data_path, "X_test.csv")
)


y_train = pd.read_csv(
    os.path.join(data_path, "y_train.csv")
)["Price"]


y_test = pd.read_csv(
    os.path.join(data_path, "y_test.csv")
)["Price"]



print("\nTraining Data Shape :", X_train.shape)
print("Testing Data Shape  :", X_test.shape)



# ============================================================
# DEFINE MODELS
# ============================================================

models = {


    "Linear Regression":

        LinearRegression(),



    "Decision Tree":

        DecisionTreeRegressor(
            random_state=42,
            max_depth=15
        ),



    "Random Forest":

        RandomForestRegressor(

            n_estimators=300,

            random_state=42,

            n_jobs=-1

        ),



    "Gradient Boosting":

        GradientBoostingRegressor(

            n_estimators=300,

            learning_rate=0.05,

            random_state=42

        ),



    "Extra Trees":

        ExtraTreesRegressor(

            n_estimators=300,

            random_state=42,

            n_jobs=-1

        )

}



# ============================================================
# TRAIN MODELS
# ============================================================


results = []


best_model = None

best_model_name = None

best_score = -1



for name, model in models.items():


    print("\n")
    print("=" * 60)

    print("Training :", name)

    print("=" * 60)



    # Train

    model.fit(
        X_train,
        y_train
    )



    # Prediction

    train_prediction = model.predict(
        X_train
    )


    test_prediction = model.predict(
        X_test
    )



    # Evaluation

    train_r2 = r2_score(
        y_train,
        train_prediction
    )


    test_r2 = r2_score(
        y_test,
        test_prediction
    )


    mae = mean_absolute_error(
        y_test,
        test_prediction
    )


    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            test_prediction
        )
    )



    print("Training R² :", round(train_r2,4))

    print("Testing R²  :", round(test_r2,4))

    print("MAE         :", round(mae,2))

    print("RMSE        :", round(rmse,2))



    results.append([

        name,

        train_r2,

        test_r2,

        mae,

        rmse

    ])




    # Best Model Selection

    if test_r2 > best_score:

        best_score = test_r2

        best_model = model

        best_model_name = name



# ============================================================
# MODEL COMPARISON
# ============================================================


results_df = pd.DataFrame(

    results,

    columns=[

        "Model",

        "Training R2",

        "Testing R2",

        "MAE",

        "RMSE"

    ]

)



results_df = results_df.sort_values(

    by="Testing R2",

    ascending=False

)



print("\n")

print("=" * 80)

print("MODEL COMPARISON")

print("=" * 80)


print(results_df)



# ============================================================
# BEST MODEL DETAILS
# ============================================================


print("\n")

print("=" * 70)

print("BEST MODEL")

print("=" * 70)



print("Model      :", best_model_name)

print("Testing R² :", round(best_score,4))



# ============================================================
# SAVE MODEL
# ============================================================


model_path = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\models"


os.makedirs(

    model_path,

    exist_ok=True

)



# Save trained model

joblib.dump(

    best_model,

    os.path.join(
        model_path,
        "best_model.pkl"
    )

)



# Save model name

joblib.dump(

    best_model_name,

    os.path.join(
        model_path,
        "best_model_name.pkl"
    )

)



print("\nBest Model Saved Successfully")



# ============================================================
# FEATURE IMPORTANCE
# ============================================================


if hasattr(best_model, "feature_importances_"):


    feature_importance = pd.DataFrame({

        "Feature":

        X_train.columns,


        "Importance":

        best_model.feature_importances_

    })



    feature_importance = feature_importance.sort_values(

        by="Importance",

        ascending=False

    )



    feature_importance.to_csv(

        os.path.join(

            data_path,

            "feature_importance.csv"

        ),

        index=False

    )



    print("Feature Importance Saved Successfully")



# ============================================================
# SAVE MODEL COMPARISON
# ============================================================


results_df.to_csv(

    os.path.join(

        data_path,

        "model_comparison.csv"

    ),

    index=False

)



print("Model Comparison Saved Successfully")



# ============================================================
# FINAL OUTPUT
# ============================================================


print("\nSaved Files")

print("✓ models/best_model.pkl")

print("✓ models/best_model_name.pkl")

print("✓ data/model_comparison.csv")

print("✓ data/feature_importance.csv")



print("\n" + "=" * 70)

print("STEP 3 COMPLETED SUCCESSFULLY")

print("=" * 70)
