import streamlit as st
import requests


def check_mushrooms():
    st.title('Mushroom Prediction')

    api_url = 'http://127.0.0.1:8000/mushroom/'

    cap_shape = st.selectbox('Cap Shape', ['b', 'c', 'f', 'k', 's', 'x'])
    cap_surface = st.selectbox('Cap Surface', ['f', 'g', 's', 'y'])
    cap_color = st.selectbox('Cap Color', ['b', 'c', 'e', 'g', 'n', 'p', 'r', 'u', 'w', 'y'])
    bruises = st.selectbox('Bruises', ['f', 't'])
    odor = st.selectbox('Odor', ['a', 'c', 'f', 'l', 'm', 'n', 'p', 's', 'y'])
    gill_attachment = st.selectbox('Gill Attachment', ['a', 'f'])
    gill_spacing = st.selectbox('Gill Spacing', ['c', 'w'])
    gill_size = st.selectbox('Gill Size', ['b', 'n'])
    gill_color = st.selectbox('Gill Color', ['b', 'e', 'g', 'h', 'k', 'n', 'o', 'p', 'r', 'u', 'w', 'y'])
    stalk_shape = st.selectbox('Stalk Shape', ['e', 't'])
    stalk_root = st.selectbox('Stalk Root', ['b', 'c', 'e', 'r', 'z'])
    stalk_surface_above_ring = st.selectbox('Stalk Surface Above Ring', ['f', 'k', 's', 'y'])
    stalk_surface_below_ring = st.selectbox('Stalk Surface Below Ring', ['f', 'k', 's', 'y'])
    stalk_color_above_ring = st.selectbox('Stalk Color Above Ring', ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'])
    stalk_color_below_ring = st.selectbox('Stalk Color Below Ring', ['b', 'c', 'e', 'g', 'n', 'o', 'p', 'w', 'y'])
    veil_color = st.selectbox('Veil Color', ['n', 'o', 'w', 'y'])
    veil_type = st.selectbox('Veil Type', ['p', 'u'])
    ring_number = st.selectbox('Ring Number', ['n', 'o', 't'])
    ring_type = st.selectbox('Ring Type', ['e', 'f', 'l', 'n', 'p'])
    spore_print_color = st.selectbox('Spore Print Color', ['b', 'h', 'k', 'n', 'o', 'r', 'u', 'w', 'y'])
    population = st.selectbox('Population', ['a', 'c', 'n', 's', 'v', 'y'])
    habitat = st.selectbox('Habitat', ['d', 'g', 'l', 'm', 'p', 'u', 'w'])

    mushroom_data = {
        "cap_shape": cap_shape,
        "cap_surface": cap_surface,
        "cap_color": cap_color,
        "bruises": bruises,
        "odor": odor,
        "gill_attachment": gill_attachment,
        "gill_spacing": gill_spacing,
        "gill_size": gill_size,
        "gill_color": gill_color,
        "stalk_shape": stalk_shape,
        "stalk_root": stalk_root,
        "stalk_surface_above_ring": stalk_surface_above_ring,
        "stalk_surface_below_ring": stalk_surface_below_ring,
        "stalk_color_above_ring": stalk_color_above_ring,
        "stalk_color_below_ring": stalk_color_below_ring,
        "veil_color": veil_color,
        "veil_type": veil_type,
        "ring_number": ring_number,
        "ring_type": ring_type,
        "spore_print_color": spore_print_color,
        "population": population,
        "habitat": habitat
    }

    if st.button('Проверить'):
        response = requests.post(api_url, json=mushroom_data)

        if response.status_code == 200:
            data = response.json()
            poisonous = data['poisonous']
            probability = data['probability']

            if poisonous == 'Yes':
                st.error(f'Ядовитый! Вероятность: {probability}')
            else:
                st.success(f'Съедобный! Вероятность: {probability}')
        else:
            st.error(f'Ошибка сервера: {response.status_code}')
            st.write(response.text)

