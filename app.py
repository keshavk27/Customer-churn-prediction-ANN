import streamlit as st
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder,OneHotEncoder
import pandas as pd
import pickle

# Page config
st.set_page_config(page_title="Churn Predictor", page_icon="📊", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background-color: #1E1E1E;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
    }
    </style>
""", unsafe_allow_html=True)

# Load model + encoders
model=tf.keras.models.load_model('model.h5')

with open('encoder.pkl','rb') as file:
    oheencodergeo=pickle.load(file)

with open('encodegender.pkl','rb') as file:
    labelencodergender=pickle.load(file)

with open('scaler.pkl','rb') as file:
    scaler=pickle.load(file)

# Title
st.markdown("<h1 style='text-align:center;'>💳 Customer Churn Prediction</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for inputs
st.sidebar.header("🧾 Customer Details")

geography = st.sidebar.selectbox('Geography', oheencodergeo.categories_[0])
gender = st.sidebar.selectbox('Gender', labelencodergender.classes_)
age = st.sidebar.slider('Age', 18, 92)
balance = st.sidebar.number_input('Balance')
credit_score = st.sidebar.number_input('Credit Score')
estimated_salary = st.sidebar.number_input('Estimated Salary')
tenure = st.sidebar.slider('Tenure', 0, 10)
num_of_products = st.sidebar.slider('Number of Products', 1, 4)
has_cr_card = st.sidebar.selectbox('Has Credit Card', [0, 1])
is_active_member = st.sidebar.selectbox('Is Active Member', [0, 1])

# Main layout
col1, col2 = st.columns([2,1])

with col1:
    st.markdown("### 📋 Input Summary")
    st.markdown(f"""
    <div class="card">
    <b>Geography:</b> {geography}<br>
    <b>Gender:</b> {gender}<br>
    <b>Age:</b> {age}<br>
    <b>Balance:</b> {balance}<br>
    <b>Credit Score:</b> {credit_score}<br>
    <b>Estimated Salary:</b> {estimated_salary}<br>
    </div>
    """, unsafe_allow_html=True)

# Prepare input
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [labelencodergender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

geo_encoded = oheencodergeo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=oheencodergeo.get_feature_names_out(['Geography']))

input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)
input_data_scaled = scaler.transform(input_data)

# Prediction button
if st.button("🔍 Predict Churn"):

    prediction = model.predict(input_data_scaled)
    prediction_proba = prediction[0][0]

    with col2:
        st.markdown("### 📊 Prediction Result")

        # Progress bar
        st.progress(float(prediction_proba))

        # Metric display
        st.metric("Churn Probability", f"{prediction_proba:.2f}")

        if prediction_proba > 0.5:
            st.error("⚠️ Customer is likely to churn")
        else:
            st.success("✅ Customer is not likely to churn")