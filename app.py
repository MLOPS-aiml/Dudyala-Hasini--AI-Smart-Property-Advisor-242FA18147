# ==========================================================
# AI SMART PROPERTY ADVISOR
# FINAL CLEAN STREAMLIT APPLICATION
# PART 1/5
# ==========================================================


# ==========================
# IMPORTS
# ==========================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

from datetime import datetime

import plotly.express as px



# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(

    page_title="AI Smart Property Advisor",

    page_icon="🏠",

    layout="wide"

)



# ==========================
# CUSTOM CSS
# ==========================

st.markdown(
"""
<style>


.main {

    background-color:#f5f9ff;

}



[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #0b3d91,
        #001f54
    );

}



[data-testid="stSidebar"] * {

    color:white;

}



.stButton button {


    width:100%;

    background:
    linear-gradient(
        90deg,
        #0072ff,
        #00c6ff
    );


    color:white;

    font-weight:bold;

    border-radius:12px;


}



div[data-testid="metric-container"] {


    background:white;

    padding:20px;

    border-radius:15px;

    box-shadow:
    0px 4px 10px #dddddd;


}



</style>
""",

unsafe_allow_html=True

)





# ==========================
# HEADER
# ==========================


st.markdown(

"""
<div style="
background:linear-gradient(90deg,#0072ff,#00c6ff);
padding:30px;
border-radius:20px;
color:white;
">


<h1 style="color:white;">
🏠 AI Smart Property Advisor
</h1>


<h3 style="color:white;">
Machine Learning Based House Price Prediction
and Smart Property Recommendation System
</h3>


</div>

""",

unsafe_allow_html=True

)






# ==========================
# PROJECT PATHS
# ==========================


BASE_PATH = r"C:\Users\HP\Desktop\AI-Smart-Property-Advisor"



MODEL_PATH = os.path.join(

    BASE_PATH,

    "models",

    "best_model.pkl"

)



DATA_PATH = os.path.join(

    BASE_PATH,

    "data",

    "Enhanced_Smart_House_Price_Dataset_New.csv"

)







# ==========================
# LOAD MODEL
# ==========================


@st.cache_resource

def load_model():


    try:

        model = joblib.load(

            MODEL_PATH

        )


        return model



    except Exception as e:


        st.error(

            f"❌ Model Loading Error : {e}"

        )


        return None







# ==========================
# LOAD DATASET
# ==========================


@st.cache_data

def load_dataset():


    try:

        data = pd.read_csv(

            DATA_PATH

        )


        return data



    except Exception as e:


        st.error(

            f"❌ Dataset Loading Error : {e}"

        )


        return None








# ==========================
# INITIALIZE MODEL + DATA
# ==========================


model = load_model()


df = load_dataset()







# ==========================
# SIDEBAR SYSTEM STATUS
# ==========================


st.sidebar.title(

    "⚙ System Status"

)



if model is not None:


    st.sidebar.success(

        "✅ AI Model Loaded Successfully"

    )

else:


    st.sidebar.error(

        "❌ Model Loading Failed"

    )





if df is not None:


    st.sidebar.success(

        "✅ Dataset Loaded Successfully"

    )


    st.sidebar.info(

        f"📊 Total Properties : {len(df):,}"

    )


else:


    st.sidebar.error(

        "❌ Dataset Loading Failed"

    )








# ==========================
# SESSION MANAGEMENT
# ==========================


if "users" not in st.session_state:


    st.session_state.users = {

        "admin":"admin123"

    }



if "logged_in" not in st.session_state:


    st.session_state.logged_in = False



if "username" not in st.session_state:


    st.session_state.username = ""



if "history" not in st.session_state:


    st.session_state.history = []



if "saved_properties" not in st.session_state:


    st.session_state.saved_properties = []



if "feedback" not in st.session_state:


    st.session_state.feedback = []

# ==========================================================
# PART 2/5
# LOGIN + CREATE ACCOUNT + LOGOUT
# ==========================================================




# ==========================================================
# CREATE ACCOUNT PAGE
# ==========================================================


def create_account_page():


    st.subheader(
        "📝 Create New Account"
    )



    username = st.text_input(

        "👤 Enter Username",

        key="new_username"

    )



    password = st.text_input(

        "🔑 Enter Password",

        type="password",

        key="new_password"

    )



    confirm_password = st.text_input(

        "🔒 Confirm Password",

        type="password",

        key="confirm_password"

    )





    if st.button(

        "✨ Create Account"

    ):



        if username == "" or password == "":


            st.warning(

                "Please fill all fields"

            )



        elif username in st.session_state.users:


            st.error(

                "Username already exists"

            )



        elif password != confirm_password:


            st.error(

                "Passwords do not match"

            )



        else:


            st.session_state.users[username] = password


            st.success(

                "✅ Account Created Successfully. Login now."

            )








# ==========================================================
# LOGIN PAGE
# ==========================================================


def login_page():


    st.markdown(

    """

    <div style="
    background:linear-gradient(90deg,#0b3d91,#0072ff);
    padding:35px;
    border-radius:20px;
    color:white;
    ">


    <h1 style="color:white;">
    🔐 Welcome to AI Smart Property Advisor
    </h1>


    <p style="color:white;">
    Login to access AI powered real estate solutions
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.write("")



    option = st.radio(

        "Choose Option",

        [

            "Login",

            "Create Account"

        ],

        horizontal=True

    )




    # ==========================
    # CREATE ACCOUNT
    # ==========================


    if option == "Create Account":


        create_account_page()





    # ==========================
    # LOGIN
    # ==========================


    else:


        username = st.text_input(

            "👤 Username"

        )



        password = st.text_input(

            "🔑 Password",

            type="password"

        )





        if st.button(

            "🚀 Login",

            use_container_width=True

        ):



            if (

                username in st.session_state.users

                and

                st.session_state.users[username] == password

            ):



                st.session_state.logged_in = True


                st.session_state.username = username



                st.success(

                    "✅ Login Successful"

                )



                st.rerun()



            else:


                st.error(

                    "❌ Invalid Username or Password"

                )









# ==========================================================
# LOGOUT FUNCTION
# ==========================================================


def logout():


    st.session_state.logged_in = False


    st.session_state.username = ""


    st.success(

        "👋 Logged out successfully"

    )


    st.rerun()

# ==========================================================
# PART 3/5
# DASHBOARD + AI HOUSE PRICE PREDICTION
# ==========================================================





# ==========================================================
# DASHBOARD PAGE
# ==========================================================


def dashboard_page():


    st.markdown(

    """
    <div style="
    background:linear-gradient(90deg,#0072ff,#00c6ff);
    padding:30px;
    border-radius:20px;
    color:white;
    ">

    <h1 style="color:white;">
    📊 AI Property Dashboard
    </h1>

    <p>
    Machine Learning Based Real Estate Analytics
    </p>

    </div>

    """,

    unsafe_allow_html=True

    )



    if df is None:

        st.error(
            "Dataset not available"
        )

        return




    st.success(

        f"Welcome {st.session_state.username} 👋"

    )



    col1,col2,col3,col4 = st.columns(4)



    with col1:

        st.metric(

            "🏠 Total Properties",

            f"{len(df):,}"

        )



    with col2:

        if "Price" in df.columns:

            avg_price = df["Price"].mean()

            st.metric(

                "💰 Average Price",

                f"${avg_price:,.0f}"

            )

        else:

            st.metric(

                "💰 Average Price",

                "N/A"

            )




    with col3:

        if "SquareFeet" in df.columns:

            st.metric(

                "📐 Average Area",

                f"{df['SquareFeet'].mean():,.0f} sqft"

            )

        else:

            st.metric(

                "📐 Average Area",

                "N/A"

            )




    with col4:

        if "PropertyScore" in df.columns:

            st.metric(

                "⭐ Property Score",

                f"{df['PropertyScore'].mean():.2f}"

            )

        else:

            st.metric(

                "⭐ Property Score",

                "N/A"

            )





    st.divider()



    if "Price" in df.columns:


        st.subheader(

            "🏠 House Price Distribution"

        )


        fig = px.histogram(

            df,

            x="Price",

            nbins=40

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )









# ==========================================================
# AI PRICE PREDICTION PAGE
# ==========================================================


def price_prediction_page():


    st.markdown(

    """
    <div style="
    background:linear-gradient(90deg,#11998e,#38ef7d);
    padding:30px;
    border-radius:20px;
    color:white;
    ">


    <h1 style="color:white;">
    💰 AI House Price Prediction
    </h1>


    <p>
    Predict property price using Machine Learning Model
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )




    if model is None:

        st.error(

            "Model not loaded"

        )

        return






    col1,col2,col3 = st.columns(3)




    with col1:


        sqft = st.number_input(

            "📐 Square Feet",

            500,

            10000,

            2000

        )



        bedrooms = st.number_input(

            "🛏 Bedrooms",

            1,

            10,

            3

        )



        bathrooms = st.number_input(

            "🚿 Bathrooms",

            1,

            10,

            2

        )






    with col2:


        neighborhood = st.selectbox(

            "📍 Neighborhood",

            df["Neighborhood"].unique()

        )



        yearbuilt = st.number_input(

            "🏗 Year Built",

            1900,

            2026,

            2015

        )



        family_score = st.slider(

            "👨‍👩‍👧 Family Suitability",

            0,

            100,

            80

        )






    with col3:


        property_score = st.slider(

            "⭐ Property Score",

            0,

            100,

            75

        )



        value_score = st.slider(

            "💎 Value Score",

            0,

            100,

            80

        )







    if st.button(

        "🔮 Predict Price",

        use_container_width=True

    ):



        try:


            house_age = 2026 - yearbuilt




            input_data = pd.DataFrame(

            [{


            "SquareFeet":sqft,


            "Bedrooms":bedrooms,


            "Bathrooms":bathrooms,


            "Neighborhood":neighborhood,


            "YearBuilt":yearbuilt,


            "HouseAge":house_age,


            "HouseSizeCategory":"Medium",


            "NeighborhoodAveragePrice":500000,


            "FamilySuitabilityScore":family_score,


            "PropertyScore":property_score,


            "ValueForMoneyScore":value_score


            }]

            )





            # Match model features automatically

            if hasattr(model,"feature_names_in_"):


                input_data = input_data.reindex(

                    columns=model.feature_names_in_,

                    fill_value=0

                )





            prediction = model.predict(

                input_data

            )[0]





            st.success(

                "✅ Prediction Completed"

            )



            st.metric(

                "🏠 Estimated Property Price",

                f"${prediction:,.2f}"

            )





            result = pd.DataFrame(

            {

            "Type":[

                "Predicted Price"

            ],

            "Price":[

                prediction

            ]

            }

            )




            fig = px.bar(

                result,

                x="Type",

                y="Price",

                title="AI Predicted House Price"

            )



            st.plotly_chart(

                fig,

                use_container_width=True

            )





            # Save History


            st.session_state.history.append(

            {


            "Date":

            datetime.now().strftime(

                "%d-%m-%Y %H:%M"

            ),


            "Square Feet":sqft,


            "Bedrooms":bedrooms,


            "Bathrooms":bathrooms,


            "Neighborhood":neighborhood,


            "Predicted Price":prediction


            }

            )





        except Exception as e:


            st.error(

                f"Prediction Error : {e}"

            )
# ==========================================================
# PART 4/5
# SMART RECOMMENDATION + INVESTMENT ANALYSIS
# ==========================================================





# ==========================================================
# SMART PROPERTY RECOMMENDATION PAGE
# ==========================================================


def recommendation_page():


    st.markdown(

    """

    <div style="
    background:linear-gradient(90deg,#ff9966,#ff5e62);
    padding:30px;
    border-radius:20px;
    color:white;
    ">


    <h1 style="color:white;">
    🏡 Smart Property Recommendation
    </h1>


    <p>
    AI recommends the best properties based on your requirements
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )



    if df is None:

        st.error(
            "Dataset not loaded"
        )

        return




    col1,col2,col3 = st.columns(3)



    with col1:

        budget = st.number_input(

            "💰 Maximum Budget",

            100000,

            10000000,

            600000

        )



    with col2:

        min_bedrooms = st.number_input(

            "🛏 Minimum Bedrooms",

            1,

            10,

            3

        )



    with col3:

        min_bathrooms = st.number_input(

            "🚿 Minimum Bathrooms",

            1,

            10,

            2

        )





    if st.button(

        "🔍 Find Best Properties",

        use_container_width=True

    ):



        try:


            filtered = df.copy()



            # Apply filters safely


            if "Price" in filtered.columns:


                filtered = filtered[

                    filtered["Price"] <= budget

                ]



            if "Bedrooms" in filtered.columns:


                filtered = filtered[

                    filtered["Bedrooms"] >= min_bedrooms

                ]



            if "Bathrooms" in filtered.columns:


                filtered = filtered[

                    filtered["Bathrooms"] >= min_bathrooms

                ]





            if len(filtered)==0:


                st.warning(

                    "No properties found. Increase budget."

                )

                return





            # AI Ranking


            if "PropertyScore" in filtered.columns:


                filtered["AI_Score"] = filtered["PropertyScore"]



            elif "Price" in filtered.columns:


                filtered["AI_Score"] = (

                    100 -

                    (

                    filtered["Price"]

                    /

                    filtered["Price"].max()

                    *

                    100

                    )

                )


            else:


                filtered["AI_Score"] = 50






            recommended = filtered.sort_values(

                "AI_Score",

                ascending=False

            ).head(5)






            st.success(

                "✅ Top 5 AI Recommended Properties"

            )




            for index,row in recommended.iterrows():


                st.divider()



                st.subheader(

                    f"🏠 Property {index}"

                )



                c1,c2,c3,c4 = st.columns(4)



                with c1:

                    st.write(

                        "📍",

                        row.get(

                            "Neighborhood",

                            "Unknown"

                        )

                    )



                with c2:

                    st.write(

                        "💰",

                        f"${row.get('Price',0):,.0f}"

                    )



                with c3:

                    st.write(

                        "🛏",

                        row.get(

                            "Bedrooms",

                            "N/A"

                        )

                    )



                with c4:

                    st.write(

                        "⭐",

                        f"{row['AI_Score']:.2f}"

                    )





                if st.button(

                    f"❤️ Save Property {index}",

                    key=f"save_{index}"

                ):



                    st.session_state.saved_properties.append(

                    {


                    "Property ID":index,


                    "Neighborhood":

                    row.get("Neighborhood",""),


                    "Price":

                    row.get("Price",0),


                    "Bedrooms":

                    row.get("Bedrooms",0),


                    "Bathrooms":

                    row.get("Bathrooms",0),


                    "AI Score":

                    row["AI_Score"]


                    }

                    )



                    st.success(

                        "Property Saved ❤️"

                    )







            if "Neighborhood" in recommended.columns:


                fig = px.bar(

                    recommended,

                    x="Neighborhood",

                    y="Price",

                    title="Recommended Property Prices"

                )


                st.plotly_chart(

                    fig,

                    use_container_width=True

                )






        except Exception as e:


            st.error(

                f"Recommendation Error : {e}"

            )









# ==========================================================
# INVESTMENT ANALYSIS PAGE
# ==========================================================


def investment_analysis_page():



    st.markdown(

    """

    <div style="
    background:linear-gradient(90deg,#8e2de2,#4a00e0);
    padding:30px;
    border-radius:20px;
    color:white;
    ">


    <h1 style="color:white;">
    📈 Property Investment Analysis
    </h1>


    <p>
    Analyze property investment opportunities using AI insights
    </p>


    </div>

    """,

    unsafe_allow_html=True

    )





    if df is None:


        st.error(

            "Dataset not loaded"

        )

        return






    location = st.selectbox(

        "📍 Select Neighborhood",

        df["Neighborhood"].unique()

    )




    location_data = df[

        df["Neighborhood"] == location

    ]





    # Average Price


    avg_price = location_data["Price"].mean()





    # Dynamic scoring


    if "PropertyScore" in location_data.columns:


        property_score = location_data["PropertyScore"].mean()


    else:


        property_score = 75





    if "ValueForMoneyScore" in location_data.columns:


        value_score = location_data["ValueForMoneyScore"].mean()


    else:


        value_score = 75






    investment_score = (

        property_score * 0.6

        +

        value_score * 0.4

    )







    col1,col2,col3 = st.columns(3)



    with col1:


        st.metric(

            "💰 Average Price",

            f"${avg_price:,.0f}"

        )



    with col2:


        st.metric(

            "⭐ Property Score",

            f"{property_score:.2f}"

        )



    with col3:


        st.metric(

            "📈 Investment Score",

            f"{investment_score:.2f}"

        )







    chart_data = pd.DataFrame(

    {


    "Category":

    [

        "Property Score",

        "Value Score",

        "Investment Score"

    ],


    "Score":

    [

        property_score,

        value_score,

        investment_score

    ]


    }

    )






    fig = px.bar(

        chart_data,

        x="Category",

        y="Score",

        title="AI Investment Analysis"

    )



    st.plotly_chart(

        fig,

        use_container_width=True

    )





    st.subheader(

        "🤖 AI Recommendation"

    )



    if investment_score >=80:


        st.success(

            "🔥 Excellent investment opportunity"

        )


    elif investment_score >=60:


        st.info(

            "👍 Good investment opportunity"

        )


    else:


        st.warning(

            "⚠ Analyse carefully before investment"

        )
# ==========================================================
# PART 5/5
# PROFILE + SAVED + HISTORY + FEEDBACK + NAVIGATION
# ==========================================================





# ==========================================================
# PROFILE PAGE
# ==========================================================


def profile_page():


    st.markdown(

    """

    <div style="
    background:linear-gradient(90deg,#667eea,#764ba2);
    padding:30px;
    border-radius:20px;
    color:white;
    ">


    <h1 style="color:white;">
    👤 User Profile
    </h1>


    </div>

    """,

    unsafe_allow_html=True

    )



    st.success(

        f"Welcome {st.session_state.username} 👋"

    )



    col1,col2 = st.columns(2)



    with col1:


        st.info(

        f"""

        👤 Account Details


        Username:

        {st.session_state.username}


        Status:

        Active User


        """

        )




    with col2:


        st.info(

        """

        🏠 AI Smart Property Advisor


        Machine Learning Based

        Real Estate Prediction System


        """

        )









# ==========================================================
# SAVED PROPERTIES PAGE
# ==========================================================


def saved_properties_page():


    st.title(

        "❤️ Saved Properties"

    )



    if len(st.session_state.saved_properties)==0:


        st.info(

            "No saved properties available"

        )


    else:


        saved_df = pd.DataFrame(

            st.session_state.saved_properties

        )


        st.dataframe(

            saved_df,

            use_container_width=True

        )



        st.download_button(

            "📄 Download Saved Properties",

            saved_df.to_csv(index=False),

            "Saved_Properties.csv"

        )









# ==========================================================
# PREDICTION HISTORY PAGE
# ==========================================================


def history_page():


    st.title(

        "🕒 Prediction History"

    )



    if len(st.session_state.history)==0:


        st.info(

            "No prediction history available"

        )


    else:


        history_df = pd.DataFrame(

            st.session_state.history

        )



        st.dataframe(

            history_df,

            use_container_width=True

        )



        st.download_button(

            "📄 Download History",

            history_df.to_csv(index=False),

            "Prediction_History.csv"

        )









# ==========================================================
# FEEDBACK PAGE
# ==========================================================


def feedback_page():


    st.title(

        "⭐ User Feedback"

    )



    rating = st.slider(

        "Rate Application",

        1,

        5,

        5

    )



    message = st.text_area(

        "Write your feedback"

    )





    if st.button(

        "Submit Feedback"

    ):



        st.session_state.feedback.append(

        {


        "User":

        st.session_state.username,


        "Rating":

        rating,


        "Feedback":

        message,


        "Date":

        datetime.now().strftime(

            "%d-%m-%Y %H:%M"

        )


        }

        )



        st.success(

            "✅ Thank you for your feedback"

        )







    if len(st.session_state.feedback)>0:


        st.subheader(

            "Previous Feedback"

        )


        st.dataframe(

            pd.DataFrame(

                st.session_state.feedback

            ),

            use_container_width=True

        )









# ==========================================================
# ABOUT PROJECT PAGE
# ==========================================================


def about_page():


    st.title(

        "🤖 About AI Smart Property Advisor"

    )


    st.write(

    """

## 🏠 AI Smart Property Advisor


An Artificial Intelligence based real estate

prediction and recommendation application.



### Features:


✅ AI House Price Prediction


✅ Smart Property Recommendation


✅ Property Investment Analysis


✅ User Account Management


✅ Saved Properties


✅ Feedback System



### Technologies Used:


🐍 Python


🎨 Streamlit


📊 Pandas


🤖 Scikit-learn


📈 Plotly



### Developed By:


Dudyala Hasini


    """

    )








# ==========================================================
# FINAL APPLICATION ROUTING
# ==========================================================


if not st.session_state.logged_in:


    login_page()



else:



    st.sidebar.markdown(

    """

    ## 🏠 AI Property Advisor

    """,

    unsafe_allow_html=True

    )



    st.sidebar.write(

        f"👤 User : {st.session_state.username}"

    )




    menu = st.sidebar.radio(

        "Navigation",

        [

        "📊 Dashboard",

        "💰 Price Prediction",

        "🏡 Property Recommendation",

        "📈 Investment Analysis",

        "❤️ Saved Properties",

        "🕒 Prediction History",

        "⭐ Feedback",

        "👤 Profile",

        "🤖 About Project",

        "🚪 Logout"

        ]

    )







    if menu=="📊 Dashboard":


        dashboard_page()




    elif menu=="💰 Price Prediction":


        price_prediction_page()




    elif menu=="🏡 Property Recommendation":


        recommendation_page()




    elif menu=="📈 Investment Analysis":


        investment_analysis_page()




    elif menu=="❤️ Saved Properties":


        saved_properties_page()




    elif menu=="🕒 Prediction History":


        history_page()




    elif menu=="⭐ Feedback":


        feedback_page()




    elif menu=="👤 Profile":


        profile_page()




    elif menu=="🤖 About Project":


        about_page()




    elif menu=="🚪 Logout":


        logout()









# ==========================================================
# FOOTER
# ==========================================================


st.markdown(

"""

<hr>

<center>


<h3>
🏠 AI Smart Property Advisor
</h3>


<p>

Machine Learning Based Real Estate Prediction System

<br>

Python | Streamlit | Scikit-learn

</p>


</center>

""",

unsafe_allow_html=True

)