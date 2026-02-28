import streamlit as st
import requests


def check_person():
    st.title('Titanic Projects')

    api_url = 'http://127.0.0.1:8000/titanic/'

    Pclass = st.number_input('классы', min_value=1, max_value=3)
    Sex = st.selectbox('Пол', ['male', 'female'])
    age = st.number_input('Возрост', min_value=0, max_value=100)
    Fare = st.number_input('Цена билета', min_value=1)
    embarked = st.selectbox('Группа', ['C', 'S', 'Q'])
    SibSp = st.number_input('Родственики', min_value=0)
    Parch = st.number_input('Родители', min_value=0, max_value=1)

    titanic_data = {
        'Pclass': Pclass,
        'Sex': Sex,
        'age': age,
        'Fare': Fare,
        'embarked': embarked,
        'SibSp': SibSp,
        'Parch': Parch

    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=titanic_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Результат: {result['Answer']}")
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключитьсся к API')