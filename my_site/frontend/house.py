import streamlit as st
import requests


def check_house():
    st.title('House Projects')

    api_url = 'http://127.0.0.1:8000/house/'

    GrLivArea = st.number_input('Область доступа', min_value=0)
    YearBuilt = st.number_input('Построенный в прошлом году', min_value=0)
    GarageCars = st.number_input('Гаражные автомобили', min_value=0)
    TotalBsmtSF = st.number_input('Всего BSMTSF', min_value=0)
    FullBath = st.number_input('Полная ванна', min_value=0)
    OverallQual = st.number_input('Общее качество', min_value=0)
    Neighborhood = st.selectbox('Соседство', ['Blueste', 'BrDale', 'BrkSide', 'ClearCr', 'CollgCr', 'Crawfor', 'Edwards', 'Gilbert',
                     'IDOTRR', 'MeadowV', 'Mitchel', 'NAmes', 'NPkVill', 'NWAmes', 'NoRidge', 'NridgHt',
                     'OldTown', 'SWISU', 'Sawyer', 'SawyerW', 'Somerst', 'StoneBr', 'Timber', 'Veenker', 'Blmngtn'])


    features = {
        'GrLivArea': GrLivArea,
        'YearBuilt': YearBuilt,
        'GarageCars': GarageCars,
        'TotalBsmtSF': TotalBsmtSF,
        'FullBath': FullBath,
        'OverallQual': OverallQual,
        'Neighborhood': Neighborhood
    }


    if st.button('Проверка'):
        try:
            answer = requests.post(api_url, json=features, timeout=10)
            if answer.status_code == 200:
                result = answer.json()
                st.success(f'Результат: {result.get('predicted_price')}')
            else:
                st.error(f'Ошибка: {answer.status_code}')
        except requests.exceptions.RequestException:
            st.error('Не удалось подключитьсся к API')









