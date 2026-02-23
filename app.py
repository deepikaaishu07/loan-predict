import streamlit as st
import joblib
import pandas as pd

model = joblib.load("loan_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Loan Amount Prediction App")

dependents = st.number_input("Number of Dependents", 0, 10)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Annual Income")
cibil = st.number_input("CIBIL Score", 300, 900)
res_asset = st.number_input("Residential Asset Value")
com_asset = st.number_input("Commercial Asset Value")
lux_asset = st.number_input("Luxury Asset Value")
bank_asset = st.number_input("Bank Asset Value")
loan_term = st.number_input("Loan Term (years)", 1, 30)

education = 1 if education == "Graduate" else 0
self_emp = 1 if self_emp == "Yes" else 0

if st.button("Predict Loan Amount"):
    data = pd.DataFrame([[dependents, education, self_emp, income, cibil,
                          res_asset, com_asset, lux_asset, bank_asset, loan_term]],
                        columns=columns)

    prediction = model.predict(data)
    st.success(f"Predicted Loan Amount: ₹ {int(prediction[0])}")