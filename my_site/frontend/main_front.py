import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from bank_front import check_bank
from titanic import check_person
from mushroom import check_mushrooms
from avacado import check_avacado
from diabetes import check_diabetes
from telecom import check_telecom
from house import check_house
from student import check_student
from hreployee import check_hremployee

with st.sidebar:
    name = st.radio('ML model:', ['Info', 'Bank', 'Titanic', 'Mushroom',
                                  'Avacado', 'Diabetes', 'Telecom', 'House', 'Student', 'HREmployee'])


if name == 'Info':
    st.title('Welcome')
    st.text('Student - предсказание успеваемости студентов')
    st.text('Bank - банковская аналитика')
    st.text('Titanic - предсказание выживаемости на Титанике')
    st.text('House - предсказание стоимости недвижимости')
    st.text('Diabetes - диогностика диабета')
    st.text('Telecom - отток клиентов телекома')
    st.text('Mushroom - класиыикасия грибов')
    st.text('Avacado - предсказание цен на авокадо')
    st.text('HREmployee - предсказание работников об уволнение')

elif name == 'Bank':
    check_bank()

elif name == 'Titanic':
    check_person()

elif name == 'Mushroom':
    check_mushrooms()

elif name == 'Avacado':
    check_avacado()

elif name == 'Diabetes':
    check_diabetes()

elif name == 'Telecom':
    check_telecom()

elif name == 'House':
    check_house()

elif name == 'Student':
    check_student()

elif name == 'HREmployee':
    check_hremployee()