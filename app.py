# 1 is good lower risk & 0 is bad higher risk 
import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load("best_extra_trees_model.pkl")
encoders={col: joblib.load(f"{col}_encoder.pkl") for col in ['Sex','Housing','Saving accounts','Checking account']}


st.title("Credit Risk Assessment App")
st.write("Enter applicant information to predict if the credit risk is good or bad ")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
sex = st.selectbox("Sex", options=['male', 'female'])
job=st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", options=['own', 'rent', 'free'])
saving_accounts = st.selectbox("Saving accounts", options=['little', 'moderate', 'rich','quite rich'])
checking_account = st.selectbox("Checking account", options=['little', 'moderate', 'rich'])
credit_amount = st.number_input("Credit amount", min_value=0, value=1000)
duration = st.number_input("Duration (in months)", min_value=1, value=12)


input_df = pd.DataFrame({
    'Age': [age],
    'Sex': [encoders['Sex'].transform([sex])[0]],
    'Job': [job],
    'Housing': [encoders['Housing'].transform([housing])[0]],
    'Saving accounts': [encoders['Saving accounts'].transform([saving_accounts])[0]],
    'Checking account': [encoders['Checking account'].transform([checking_account])[0]],
    'Credit amount': [credit_amount],
    'Duration': [duration]
})

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]
    if pred == 1:
        st.success("The credit risk is : **Good (low risk)**")
    else:
        st.error("The credit risk is : **Bad (high risk)**")