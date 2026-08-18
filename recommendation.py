# ============================================================
# AI SMART PROPERTY ADVISOR
# STEP 7 - PROPERTY RECOMMENDATION SYSTEM
# ============================================================

import pandas as pd


print("=" * 70)
print("AI SMART PROPERTY ADVISOR")
print("STEP 7 : PROPERTY RECOMMENDATION SYSTEM")
print("=" * 70)



# ============================================================
# LOAD PROCESSED DATASET
# ============================================================


df = pd.read_csv(
    "../data/processed_property_data_New.csv"
)


print("\nDataset Loaded Successfully")


print("Dataset Shape :", df.shape)



# ============================================================
# USER REQUIREMENTS
# ============================================================


budget = 600000

minimum_bedrooms = 3

minimum_bathrooms = 2



print("\nUSER REQUIREMENTS")

print("-" * 70)


print(
    f"Maximum Budget    : ₹ {budget:,.2f}"
)


print(
    f"Minimum Bedrooms  : {minimum_bedrooms}"
)


print(
    f"Minimum Bathrooms : {minimum_bathrooms}"
)



# ============================================================
# FILTER PROPERTIES
# ============================================================


recommended_properties = df[

    (df["Price"] <= budget)

    &

    (df["Bedrooms"] >= minimum_bedrooms)

    &

    (df["Bathrooms"] >= minimum_bathrooms)

]



# ============================================================
# SMART RECOMMENDATION SCORE
# ============================================================


if not recommended_properties.empty:


    recommended_properties = recommended_properties.copy()



    recommended_properties["RecommendationScore"] = (

        recommended_properties["PropertyScore"] * 0.35

        +

        recommended_properties["LocationScore"] * 0.25

        +

        recommended_properties["LuxuryScore"] * 0.20

        +

        recommended_properties["EnergyScore"] * 0.20

    )



    recommended_properties = recommended_properties.sort_values(

        by="RecommendationScore",

        ascending=False

    )



# ============================================================
# DISPLAY RESULTS
# ============================================================


print("\n" + "=" * 70)

print("TOP RECOMMENDED PROPERTIES")

print("=" * 70)



if recommended_properties.empty:


    print(
        "No properties found for the selected criteria."
    )


else:


    print(
        f"Total Matching Properties : {len(recommended_properties)}"
    )


    print("\nTop 10 Properties:\n")



    print(

        recommended_properties[

            [

                "SquareFeet",

                "Bedrooms",

                "Bathrooms",

                "Neighborhood",

                "YearBuilt",

                "Price",

                "RecommendationScore"

            ]

        ].head(10)

    )



# ============================================================
# SAVE RECOMMENDATIONS
# ============================================================


recommended_properties.head(10).to_csv(

    "../data/recommended_properties.csv",

    index=False

)



print("\nRecommendation Results Saved")

print(
    "File : data/recommended_properties.csv"
)



print("\nRecommendation Completed Successfully!")

print("=" * 70)

print("STEP 7 COMPLETED SUCCESSFULLY")

print("=" * 70)
