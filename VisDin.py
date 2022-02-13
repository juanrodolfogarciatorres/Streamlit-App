# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:08:21 2022

@author: jgarcia
"""
import pandas as pd
import streamlit as st
from app_functions import *
from PIL import Image


st.set_page_config(page_title='Dashboard Powerlifting')
st.title('Dashboard Powerlifting')

st.sidebar.header('Elegir entre: ')
menu = st.sidebar.selectbox(
    "Opciones",
    ("Datos", "Competiciones", "Competidores", "Equipamiento"),)


if menu == 'Datos':
    image = Image.open('imagendatos.jpg')
    st.image(image, caption='Los datos son sólo el comienzo')
    set_datos()
    
elif menu == 'Competiciones':
    set_competiciones()
    
elif menu == 'Competidores':
    set_competidores()
    
elif menu == 'Equipamiento':
    set_equipamiento()