import streamlit as st
import requests


def check_telecom():
    st.title("Telecom Churn Prediction")

    api_url = "http://127.0.0.1:8000/telecom/"


    gender_list = ['Female', 'Male']
    Partner_list = ['Yes', 'No']
    Dependents_list = ['No', 'Yes']
    PhoneService_list = ['No', 'Yes']
    MultipleLines_list = ['No phone service', 'No', 'Yes']
    InternetService_list = ['DSL', 'Fiber optic', 'No']
    OnlineSecurity_list = ['No', 'Yes', 'No internet service']
    OnlineBackup_list = ['Yes', 'No', 'No internet service']
    DeviceProtection_list = ['No', 'Yes', 'No internet service']
    TechSupport_list = ['No', 'Yes', 'No internet service']
    StreamingTV_list = ['No', 'Yes', 'No internet service']
    StreamingMovies_list = ['No', 'Yes', 'No internet service']
    Contract_list = ['Month-to-month', 'One year', 'Two year']
    PaperlessBilling_list = ['Yes', 'No']
    PaymentMethod_list = [
        'Electronic check',
        'Mailed check',
        'Bank transfer (automatic)',
        'Credit card (automatic)'
    ]


    gender = st.selectbox("Gender", gender_list)
    SeniorCitizen = st.number_input('SeniorCitizen', min_value=0, step=1)
    Partner = st.selectbox("Partner", Partner_list)
    Dependents = st.selectbox("Dependents", Dependents_list)
    tenure = st.number_input("Tenure (months)", min_value=0, value=12)
    PhoneService = st.selectbox("PhoneService", PhoneService_list)
    MultipleLines = st.selectbox("MultipleLines", MultipleLines_list)
    InternetService = st.selectbox("InternetService", InternetService_list)
    OnlineSecurity = st.selectbox("OnlineSecurity", OnlineSecurity_list)
    OnlineBackup = st.selectbox("OnlineBackup", OnlineBackup_list)
    DeviceProtection = st.selectbox("DeviceProtection", DeviceProtection_list)
    TechSupport = st.selectbox("TechSupport", TechSupport_list)
    StreamingTV = st.selectbox("StreamingTV", StreamingTV_list)
    StreamingMovies = st.selectbox("StreamingMovies", StreamingMovies_list)
    Contract = st.selectbox("Contract", Contract_list)
    PaperlessBilling = st.selectbox("PaperlessBilling", PaperlessBilling_list)
    PaymentMethod = st.selectbox("PaymentMethod", PaymentMethod_list)
    MonthlyCharges = st.number_input("MonthlyCharges", min_value=0.0, value=70.0)
    TotalCharges = st.number_input('TotalCharges', step=1)

    if st.button('Проверка'):

        telecom_data = {
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "tenure": tenure,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "MonthlyCharges": MonthlyCharges,
            'TotalCharges': TotalCharges

        }

        try:
            answer = requests.post(api_url, json=telecom_data, timeout=10)

            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Результат: {result.get('Answer')}")
            else:
                st.error(f"Ошибка API: {answer.status_code}")

        except requests.exceptions.RequestException:
            st.error("Не удалось подключиться к API")