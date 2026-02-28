import streamlit as st
import requests


def check_diabetes():
    st.title('Diabet Project')

    api_url = 'http://127.0.0.1:8000/diabetes/'

    Pregnancies = st.number_input('Беременности', min_value=0, max_value=9)
    Glucose = st.number_input('Глюкоза', min_value=0, step=1)
    BloodPressure = st.number_input('Давление крови', min_value=60, step=10)
    SkinThickness = st.number_input('Толщина кожи', min_value=1)
    Insulin = st.number_input('Инсулин', min_value=0)
    BMI = st.number_input('ИМТ', min_value=0.0)
    DiabetesPedigreeFunction = st.number_input('Нарушение функции почек при диабете', min_value=0.0)
    Age = st.number_input('Возрост', min_value=1, max_value=100)


    diabetes_dict = {
        'Pregnancies': Pregnancies,
        'Glucose': Glucose,
        'BloodPressure': BloodPressure,
        'SkinThickness': SkinThickness,
        'Insulin': Insulin,
        'BMI': BMI,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': Age
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=diabetes_dict, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Результат: {result['diabetes']}")
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключитьсся к API')



