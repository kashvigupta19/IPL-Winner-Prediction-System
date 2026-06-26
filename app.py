# ============================================
# IPL WINNER PREDICTION SYSTEM
# ============================================

import streamlit as st
import pandas as pd
import joblib

# ============================================
# LOAD MODEL & FILES
# ============================================

model = joblib.load("best_model.pkl")

label_encoder = joblib.load("label_encoder.pkl")

feature_names = joblib.load("feature_names.pkl")

team_strength = pd.read_csv("team_strength_dataset.csv")
model_performance = pd.read_csv("model_comparison.csv")

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="IPL Winner Prediction System",
    page_icon="🏏",
    layout="wide"
)
# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
<style>

/* Main background */
.stApp{
    background-color:#0E1117;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#1C2833;
}

/* Main title */
h1{
    color:#FFD700;
    text-align:center;
    font-weight:bold;
}

/* Sub headings */
h2,h3{
    color:#4FC3F7;
}

/* Metric cards */
div[data-testid="metric-container"]{
    background-color:#1F2937;
    border:2px solid #2E86C1;
    border-radius:15px;
    padding:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.4);
}

/* Buttons */
.stButton>button{
    background-color:#1565C0;
    color:white;
    border-radius:10px;
    font-size:18px;
    font-weight:bold;
    height:50px;
    width:100%;
}

.stButton>button:hover{
    background-color:#0D47A1;
}

/* Selectbox */
div[data-baseweb="select"]{
    border-radius:10px;
    color:black !important;
}
/* Success message */
.stSuccess{
    background-color:#1B5E20;
}

/* Info message */
.stInfo{
    background-color:#01579B;
}

/* Radio button labels */
.stRadio label {
    color: white !important;
}

/* Selectbox labels */
.stSelectbox label {
    color: white !important;
}

/* Metric labels */
div[data-testid="metric-container"] label {
    color: white !important;
}

/* Markdown text */
[data-testid="stMarkdownContainer"] {
    color: white !important;
}

/* Tables */
table {
    color: white !important;
}

/* Dataframe text */
[data-testid="stDataFrame"] {
    color: white !important;
}
/* Main title */
h1 {
    color: #FFD700 !important;   /* Gold */
    text-align: center;
    font-weight: bold;
}

/* Sub-headings */
h2, h3 {
    color: #00E5FF !important;   /* Bright Cyan */
}

/* Smaller headings */
h4, h5, h6 {
    color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)
   

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🏏 IPL Predictor")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🏆 Predict Winner",
        "📊 Team Analysis",
        "🤖 Model Performance",
        "ℹ️ About"
    ]
)

# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------

if page == "🏠 Home":

    st.title("🏏 IPL Winner Prediction System")

    st.subheader("Artificial Intelligence & Machine Learning Project")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Teams", "10")

    with col2:
        st.metric("Synthetic Matches", "5000")

    with col3:
        st.metric("ML Models", "4")

    st.markdown("---")

    st.header("📌 Project Overview")

    st.write("""
This project predicts the winning team of an IPL match using Machine Learning.

The project includes:

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)

It compares all models and selects the best-performing model for predictions.
""")

    st.success("Select an option from the left sidebar to continue.")

# -------------------------------------------------
# PLACEHOLDER PAGES
# -------------------------------------------------

elif page == "🏆 Predict Winner":

    st.title("🏆 IPL Match Winner Prediction")

    st.markdown("---")

    teams = sorted(team_strength["Team"].unique())

    venues = [
        "Wankhede Stadium",
        "Eden Gardens",
        "Chepauk",
        "Chinnaswamy Stadium",
        "Narendra Modi Stadium",
        "Arun Jaitley Stadium",
        "Rajiv Gandhi Stadium",
        "Ekana Stadium"
    ]

    weather = [
        "Sunny",
        "Cloudy",
        "Humid",
        "Dew"
    ]

    toss_decision = [
        "Bat",
        "Field"
    ]

    col1, col2 = st.columns(2)

    with col1:

        team1 = st.selectbox(
            "Select Team 1",
            teams
        )

        venue = st.selectbox(
            "Venue",
            venues
        )
        toss = st.selectbox(
            "Toss Winner",
                teams
        )

        available_teams = [team for team in teams if team != team1]

        
        

    with col2:

        team2 = st.selectbox(
            "Select Team 2",
            available_teams
        )

        weather_selected = st.selectbox(
            "Weather",
            weather
        )

        decision = st.selectbox(
            "Toss Decision",
            toss_decision
        )

    if team1 == team2:

        st.error("Please choose two different teams.")

    else:

        strength1 = float(
            team_strength.loc[
                team_strength["Team"] == team1,
                "Overall_Strength"
            ].values[0]
        )

        strength2 = float(
            team_strength.loc[
                team_strength["Team"] == team2,
                "Overall_Strength"
            ].values[0]
        )
        st.markdown("---")

        st.subheader("📈 Match Conditions")

        col3, col4 = st.columns(2)

        with col3:

            form1 = st.slider(
             "Recent Form - Team 1",
             min_value=0,
             max_value=100,
             value=75
            )

            home_advantage = st.slider(
             "Home Advantage",
            min_value=0,
                max_value=10,
                value=5
             )

        with col4:

            form2 = st.slider(
              "Recent Form - Team 2",
                  min_value=0,
              max_value=100,
              value=75
            )

        if st.button("Predict Winner"):

            input_data = pd.DataFrame({

                "Team1":[team1],
                "Team2":[team2],
                "Team1_Strength":[strength1],
                "Team2_Strength":[strength2],
                "Team1_Form":[form1],
                "Team2_Form":[form2],
                "Venue":[venue],
                "Weather":[weather_selected],
                "Toss_Winner":[toss],
                "Toss_Decision":[decision],
                "Home_Advantage":[home_advantage]

            })

            input_encoded = pd.get_dummies(input_data)

            input_encoded = input_encoded.reindex(
                columns=feature_names,
                fill_value=0
            )

            # Make Prediction
            prediction = model.predict(input_encoded)

            winner = label_encoder.inverse_transform(prediction)[0]

# Prediction Probabilities
            probabilities = model.predict_proba(input_encoded)[0]

            winner_index = prediction[0]

            confidence = probabilities[winner_index] * 100

# Display Result

            st.markdown("---")

            st.success(f"🏆 Predicted Winner: **{winner}**")

            st.metric(
            label="Prediction Confidence",
            value=f"{confidence:.2f}%"
            )

            st.markdown("---")

            st.subheader("Winning Probability")

            team1_index = label_encoder.transform([team1])[0]
            team2_index = label_encoder.transform([team2])[0]

            team1_probability = probabilities[team1_index] * 100
            team2_probability = probabilities[team2_index] * 100

            st.write(f"### {team1}")
            st.progress(team1_probability / 100)
            st.write(f"{team1_probability:.2f}%")

            st.write("")

            st.write(f"### {team2}")
            st.progress(team2_probability / 100)
            st.write(f"{team2_probability:.2f}%")

            st.markdown("---")

            st.subheader("📋 Match Summary")

            summary = pd.DataFrame({
                 "Feature": [
                      "Team 1",
                      "Team 2",
                      "Venue",
                      "Weather",
                      "Toss Winner",
                      "Toss Decision",
                      "Predicted Winner"
                    ],
                 "Value": [
                    team1,
                    team2,
                     venue,
                     weather_selected,
                     toss,
                     decision,
                     winner
                    ]
                })

            st.table(summary)

elif page == "📊 Team Analysis":

    st.title("📊 Team Strength Analysis")

    st.markdown("---")

    selected_team = st.selectbox(
        "Select IPL Team",
        sorted(team_strength["Team"].unique())
    )

    team = team_strength[
        team_strength["Team"] == selected_team
    ].iloc[0]

    st.header(f"🏏 {selected_team}")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Overall Strength",
            f"{team['Overall_Strength']:.2f}"
        )

        st.metric(
            "Experience",
            f"{team['Experience']:.2f}"
        )

    with col2:

        st.metric(
            "Fitness",
            f"{team['Fitness']:.2f}"
        )

    st.markdown("---")

    st.subheader("Batting Strength")

    st.progress(float(team["Batting_Strength"]) / 100)

    st.write(f"{team['Batting_Strength']:.2f}")

    st.subheader("Bowling Strength")

    st.progress(float(team["Bowling_Strength"]) / 100)

    st.write(f"{team['Bowling_Strength']:.2f}")

    st.subheader("Fielding Strength")

    st.progress(float(team["Fielding_Strength"]) / 100)

    st.write(f"{team['Fielding_Strength']:.2f}")


elif page == "🤖 Model Performance":

    st.title("🤖 Model Performance Dashboard")

    st.markdown("---")

    best_model = model_performance.loc[
        model_performance["Accuracy"].idxmax()
    ]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🏆 Best Model",
            best_model["Model"]
        )

    with col2:
        st.metric(
            "Accuracy",
            f"{best_model['Accuracy']:.4f}"
        )

    with col3:
        st.metric(
            "Precision",
            f"{best_model['Precision']:.4f}"
        )

    with col4:
        st.metric(
            "F1 Score",
            f"{best_model['F1 Score']:.4f}"
        )

    st.markdown("---")

    st.subheader("📊 Model Comparison")

    st.dataframe(
        model_performance,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("🏅 Accuracy Comparison")

    chart = model_performance.set_index("Model")["Accuracy"]

    st.bar_chart(chart)

    st.markdown("---")

    st.subheader("📈 Precision Comparison")

    chart = model_performance.set_index("Model")["Precision"]

    st.bar_chart(chart)

    st.markdown("---")

    st.subheader("🎯 Recall Comparison")

    chart = model_performance.set_index("Model")["Recall"]

    st.bar_chart(chart)

    st.markdown("---")

    st.subheader("⭐ F1 Score Comparison")

    chart = model_performance.set_index("Model")["F1 Score"]

    st.bar_chart(chart)

elif page == "ℹ️ About":

    st.title("ℹ️ About This Project")

    st.markdown("---")

    st.header("🏏 IPL Winner Prediction System")

    st.write("""
This project is an Artificial Intelligence and Machine Learning based web application
developed to predict the winning team of an IPL cricket match.

The system uses a synthetic IPL match dataset generated from player information and
predicts the winner using multiple Machine Learning algorithms.
""")

    st.markdown("---")

    st.subheader("🎯 Project Objectives")

    st.markdown("""
- Predict IPL match winners using Machine Learning.
- Compare multiple ML algorithms.
- Build an interactive web application using Streamlit.
- Analyze player ratings and team strengths.
- Visualize model performance.
""")

    st.markdown("---")

    st.subheader("🤖 Machine Learning Models Used")

    st.markdown("""
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
""")

    st.markdown("---")

    st.subheader("🛠️ Technologies Used")

    tech1, tech2 = st.columns(2)

    with tech1:
        st.markdown("""
**Programming**
- Python

**Libraries**
- Pandas
- NumPy
- Scikit-learn
- Joblib
""")

    with tech2:
        st.markdown("""
**Visualization**
- Matplotlib
- Seaborn

**Frontend**
- Streamlit
""")

    st.markdown("---")

    st.subheader("📊 Project Features")

    st.markdown("""
✅ Data Cleaning & Preprocessing

✅ Synthetic Dataset Generation

✅ Feature Engineering

✅ Team Strength Analysis

✅ Player Ratings Dashboard

✅ Match Winner Prediction

✅ Model Comparison

✅ Feature Importance

✅ Interactive Streamlit Dashboard
""")

    st.markdown("---")

    st.subheader("📁 Dataset Information")

    st.write("""
The project uses a player dataset as the base dataset.
Since match-level information was unavailable, a realistic synthetic IPL match
dataset was generated using player ratings, team strengths, match conditions,
toss information, venue, weather, and recent team form.
""")

    st.markdown("---")

    st.success("🏆 Best Performing Model: Random Forest")

    st.info("Developed as an AI/ML Project using Python, Scikit-learn and Streamlit.")