import pandas as pd
import numpy as np

np.random.seed(42)

ROWS = 50000
CURRENT_YEAR = 2026

print("="*70)
print("AI SMART PROPERTY ADVISOR")
print("GENERATING DATASET")
print("="*70)

# --------------------------------------------------
# BASIC FEATURES
# --------------------------------------------------

square_feet = np.random.randint(600,5001,ROWS)

bedrooms = np.random.randint(1,7,ROWS)

bathrooms = np.random.randint(1,6,ROWS)

floors = np.random.randint(1,4,ROWS)

parking = np.random.randint(0,5,ROWS)

year_built = np.random.randint(1990,2026,ROWS)

balcony = np.random.randint(0,2,ROWS)

garden = np.random.randint(0,2,ROWS)

lift = np.random.randint(0,2,ROWS)

security = np.random.randint(0,2,ROWS)

power_backup = np.random.randint(0,2,ROWS)

swimming_pool = np.random.randint(0,2,ROWS)

smart_home = np.random.randint(0,2,ROWS)

solar = np.random.randint(0,2,ROWS)

green_area = np.random.randint(1,11,ROWS)

road = np.random.randint(1,11,ROWS)

amenities = np.random.randint(1,11,ROWS)

crime = np.random.randint(1,11,ROWS)

school_distance = np.random.uniform(0.5,10,ROWS)

hospital_distance = np.random.uniform(0.5,10,ROWS)

metro_distance = np.random.uniform(0.5,12,ROWS)

neighborhood = np.random.choice(
    [
        "Urban",
        "Suburban",
        "Rural"
    ],
    ROWS,
    p=[0.45,0.40,0.15]
)

property_type = np.random.choice(
    [
        "Apartment",
        "Villa",
        "Independent House"
    ],
    ROWS,
    p=[0.45,0.25,0.30]
)

house_age = CURRENT_YEAR-year_built

total_rooms = bedrooms+bathrooms

# --------------------------------------------------
# ADVANCED FEATURE ENGINEERING
# --------------------------------------------------

house_size_category = []

for sqft in square_feet:
    if sqft < 1000:
        house_size_category.append("Small")
    elif sqft < 2000:
        house_size_category.append("Medium")
    elif sqft < 3500:
        house_size_category.append("Large")
    else:
        house_size_category.append("Luxury")

family_score = (
    bedrooms * 4 +
    bathrooms * 3 +
    parking * 2 +
    garden * 2 +
    balcony
)

location_score = (
    amenities * 4 +
    road * 3 +
    green_area * 2 -
    crime * 2
)

luxury_score = (
    smart_home * 20 +
    swimming_pool * 18 +
    lift * 15 +
    solar * 12 +
    security * 15 +
    power_backup * 10
)

accessibility_score = (
    100
    - school_distance * 2
    - hospital_distance * 2
    - metro_distance
)

property_score = (
    family_score +
    luxury_score +
    location_score +
    accessibility_score
)

energy_score = (
    solar * 30 +
    smart_home * 20 +
    green_area * 5
)
# --------------------------------------------------
# NONLINEAR PRICE CALCULATION
# --------------------------------------------------

base_price = (
    square_feet ** 1.08 * 95
)

price = (
    base_price

    + (bedrooms ** 2) * 12000

    + np.sqrt(bathrooms) * 30000

    + (parking + 1) ** 2 * 8000

    + np.log1p(square_feet) * 45000

    + (luxury_score ** 1.2) * 180

    + (location_score ** 2) * 120

    + (family_score ** 1.5) * 200

    - (house_age ** 1.3) * 120

    - (crime ** 2) * 2500

    + np.sin(square_feet / 500) * 15000

    + np.cos(road) * 8000

    + np.random.normal(0, 12000, ROWS)
)

price = price.astype(int)

price = np.where(price < 300000, 300000, price)

# --------------------------------------------------
# CREATE DATAFRAME
# --------------------------------------------------

df = pd.DataFrame({

    "SquareFeet": square_feet,
    "Bedrooms": bedrooms,
    "Bathrooms": bathrooms,
    "Floors": floors,
    "ParkingSpaces": parking,

    "YearBuilt": year_built,
    "HouseAge": house_age,

    "Neighborhood": neighborhood,
    "PropertyType": property_type,

    "Balcony": balcony,
    "Garden": garden,
    "Lift": lift,
    "Security": security,
    "PowerBackup": power_backup,
    "SwimmingPool": swimming_pool,
    "SmartHome": smart_home,
    "SolarPanels": solar,

    "GreenAreaScore": green_area,
    "RoadConnectivity": road,
    "AmenitiesScore": amenities,
    "CrimeIndex": crime,

    "SchoolDistance": school_distance.round(2),
    "HospitalDistance": hospital_distance.round(2),
    "MetroDistance": metro_distance.round(2),

    "TotalRooms": total_rooms,
    "FamilySuitabilityScore": family_score,
    "LocationScore": location_score,
    "LuxuryScore": luxury_score,
    "AccessibilityScore": accessibility_score.round(2),
    "PropertyScore": property_score.round(2),
    "EnergyScore": energy_score,

    "HouseSizeCategory": house_size_category,

    "Price": price

})

# --------------------------------------------------
# SHUFFLE DATASET
# --------------------------------------------------

df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# --------------------------------------------------
# SAVE CSV
# --------------------------------------------------

output_file = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor\data\Enhanced_Smart_House_Price_Dataset_New.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n" + "="*70)
print("DATASET GENERATED SUCCESSFULLY")
print("="*70)

print(df.head())

print("\nRows    :", df.shape[0])
print("Columns :", df.shape[1])

print("\nSaved File :", output_file)

print("="*70)
