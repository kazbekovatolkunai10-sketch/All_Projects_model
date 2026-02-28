import streamlit as st
import requests


def check_student():
    st.title('Student Project')
    api_url = 'http://127.0.0.1:8000/student/'
    gender = st.selectbox('Пол', ['male', 'female'])
    race_ethnicity = st.selectbox('Группы', ['A', 'B', 'C', 'D', 'E'])
    parental_education = st.selectbox('Родительское образование', ["bachelor's degree", 'high school', "master's degree", 'some college', 'some high school', "associate's degree"])
    lunch = st.selectbox('Oбед', ['standard', 'free/reduced'])
    test_preparation = st.selectbox('Подготовка к тесту', ['none', 'completed'])
    math_score = st.number_input('Баллы по математике', min_value=0, max_value=200, step=10)
    reading_score = st.number_input('Баллы по чтению', min_value=0, max_value=200, step=10)

    student_data = {
        "gender": gender,
        "race_ethnicity": race_ethnicity,
        "parental_education": parental_education,
        "lunch": lunch,
        "test_preparation": test_preparation,
        "math_score": math_score,
        "reading_score": reading_score
    }

    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=student_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.json(result)
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error(f'Не удалось подключиться к API')
