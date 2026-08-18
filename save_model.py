# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 9 - SAVE BEST MODEL VERIFICATION
# ============================================================

import os
import joblib


print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 9 : SAVE BEST MODEL VERIFICATION")
print("=" * 70)



# ============================================================
# PATHS
# ============================================================


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_FOLDER = os.path.join(
    BASE_DIR,
    "models"
)


MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "best_model.pkl"
)


MODEL_NAME_PATH = os.path.join(
    MODEL_FOLDER,
    "best_model_name.pkl"
)


os.makedirs(
    MODEL_FOLDER,
    exist_ok=True
)



# ============================================================
# CHECK MODEL FILE
# ============================================================


if os.path.exists(MODEL_PATH):


    print("\n✓ Best Model File Found")

    print(
        "Location :",
        MODEL_PATH
    )


    model = joblib.load(
        MODEL_PATH
    )


    print("\nMODEL INFORMATION")

    print("-" * 70)


    print(
        "Model Type :",
        type(model).__name__
    )



    # Save model name

    model_name = type(model).__name__


    joblib.dump(

        model_name,

        MODEL_NAME_PATH

    )


    print(
        "Model Name Saved :",
        MODEL_NAME_PATH
    )



else:


    print("\n❌ best_model.pkl not found")

    print(
        "Please run Step 3 Model Training first."
    )



# ============================================================
# FINAL STATUS
# ============================================================


print("\n" + "=" * 70)

print("STEP 9 COMPLETED SUCCESSFULLY")

print("=" * 70)
