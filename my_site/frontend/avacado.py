import streamlit as st
import requests


def check_avacado():
    st.title('Avacado Projects')

    api_url = 'http://127.0.0.1:8001/avacado/'

    firmness = st.number_input('стойкость', min_value=0.0, step=1.0)
    hue = st.number_input('оттенок', min_value=0, step=1)
    saturation = st.number_input('насыщение', min_value=0, step=1)
    brightness = st.number_input('яркость', min_value=0)
    color_category = st.selectbox('Цвет', ['blank', 'purple', 'green', 'dark_blue'])
    sound_db = st.number_input('sound_db', min_value=1, step=1)
    weight_g = st.number_input('Вес аввкады', min_value=1)
    size_cm3 = st.number_input('Длина', min_value=1, step=1)


    avacado_data = {
        'firmness': firmness,
        'hue': hue,
        'saturation': saturation,
        'brightness': brightness,
        'color_category': color_category,
        'sound_db': sound_db,
        'weight_g': weight_g,
        'size_cm3': size_cm3
    }


    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=avacado_data, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f"Результат: {result['predict']}")
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключитьсся к API')







