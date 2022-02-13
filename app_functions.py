# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 17:50:32 2022

@author: jgarcia
"""

import streamlit as st
import pandas as pd
import numpy as np
from plotnine import *
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.graph_objects as go

#cargamos los datos
meets = pd.read_csv('meets_clean.csv')
powerlifting = pd.read_csv('power_clean.csv')

filtro = powerlifting['Age'] > 0
powerlifting = powerlifting[filtro]


def set_datos():
    choice=st.radio('Elige una base de datos', ('Encuentros', 'Levantamiento de pesas'))
    
    if choice== 'Encuentros':
        st.write('Has elegido la base datos acerca de las competiciones')
        st.dataframe(meets)
        with st.expander('Federaciones que participan'):
            st.write(meets['Federation'].unique())
        
        with st.expander('Paises donde se celebra'):
            st.write(meets['MeetCountry'].unique())
        
        with st.expander('Estados donde se celebra'):
            st.write(meets['MeetState'].unique())
        
        with st.expander('Ciudades donde se celebra'):
            st.write(meets['MeetTown'].unique())       

    else:
        st.write('Has elegido la base datos acerca de las competidores')
        st.dataframe(powerlifting)
        with st.expander('Ver estadísticas'):
            st.write(powerlifting[['Age','BodyweightKg','WeightClassKg', 'BestSquatKg','BestBenchKg', 
                                  'BestDeadliftKg', 'TotalKg', 'Wilks']].describe())




def set_competiciones():
    st.subheader('¿Que federaciones participan más? ¿En qué países y ciudades?')
    st.write('En este panel puedes observar las federaciones, así como los países, estados y ciudades que más y que menos han participado en las competiciones.')
    variables = st.selectbox(
        'Elige entre:',
        ['Federaciones', 'Países', 'Estados', 'Ciudades'])
    
    if variables== 'Federaciones':
        top10_federations=meets['Federation'].value_counts().head(10)
        st.write('Federaciones que más han participado')
        st.bar_chart(top10_federations)
        top10_federaciones_que_menos=meets['Federation'].value_counts().tail(10)
        st.write('Federaciones que menos han participado')
        st.bar_chart(top10_federaciones_que_menos)
        
    elif variables == 'Países':
        pais=meets['MeetCountry'].value_counts().head(5)
        fig, ax= plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        labels= pais.index
        ax.pie(pais, labels =labels, autopct='%.0f%%')
        ax.set_title('')
        st.pyplot(fig)
        st.write('De todos los países donde se realizan competiciones se aprecia que en USA estan ubicadas más de la mitad de este tipo de eventos.')
        
    elif variables == 'Estados':
        eje_y= meets['MeetState'].value_counts().head(10)
        eje_x= eje_y.index
        fig = plt.figure(figsize = (10, 5))
        plt.barh(eje_x, eje_y, color="green")
        plt.ylabel('Estados participantes')
        plt.xlabel('Encuentros')
        plt.title('Estados más solicitados')
        st.pyplot(fig)
    
    else:
        ciudades =  meets['MeetTown'].value_counts().head(10)
        st.write('Ciudades que más han participado.')
        st.bar_chart(ciudades)
        st.write('De otro modo, estan son algunas de las ciudades en las que no se han realizado casi ninguna competición. Para ser exactos, solo una.')
        ciudades_peores = meets['MeetTown'].value_counts().tail(10)
        eje_x= ciudades_peores.index
        fig = plt.figure(figsize = (10, 5))
        plt.barh(eje_x, ciudades_peores, color="orange")
        plt.xlim(0,3)
        plt.ylabel('Ciudades participantes')
        st.pyplot(fig)


def set_competidores():
    st.header('')
    st.subheader('Analizamos las estadísticas de los participantes')
    choice = st.selectbox('', ('Edad', 'Peso levantado en cada ejercicio', 'Peso total levantado'))
        
    if choice == 'Edad':
        fig, ax = plt.subplots(1, figsize=(10, 6))
        sns.kdeplot(powerlifting['Age'])
        plt.suptitle("Lifter Age Distribution")
        st.pyplot(fig)
        st.write('Observamos que la mayoría de deportistas tienen alrededor de 25 años. Incluso hay algunos deportistas con edades que sobrepasan los 80 años.')
        
    elif choice == 'Peso levantado en cada ejercicio':
        fig = plt.figure(figsize = (10, 5))
        powerlifting.query('Sex == "M"')['WeightClassKg'].str.replace("+", "").astype(float).value_counts().sort_index().plot.line()
        powerlifting.query('Sex == "F"')['WeightClassKg'].str.replace("+", "").astype(float).value_counts().sort_index().plot.line()
        plt.suptitle("Categoría según el peso")
        plt.gca().set_xlabel("Weight Class (kg)")
        plt.gca().set_ylabel("N")
        plt.legend(('Hombres', 'Mujeres'))
        st.pyplot(fig)
        st.write('Vemos que en las categorías superiores abunda el género masculino. ')
        
        #figura 2
        st.subheader('Ejercicios de peso libre')
        col1, col2, col3 = st.columns(3)
        with col1:
            choice = st.selectbox('Elige  género:', ('Hombres', 'Mujeres'))
            
        if choice == 'Hombres':
            st.write('Press de Banca')
            chart_datas = powerlifting[powerlifting.Sex=='M']['BestBenchKg']
            st.line_chart(chart_datas)
            
            st.write('Sentadilla')
            BestBM = powerlifting[powerlifting.Sex=='M']['BestSquatKg']
            st.line_chart(BestBM)
            
            st.write('Peso muerto')
            Deadkg = powerlifting[powerlifting.Sex=='M']['BestDeadliftKg']
            st.line_chart(Deadkg)
            
        else:
            st.write('Press de Banca')
            datosF = powerlifting[powerlifting.Sex=='F']['BestBenchKg']
            st.line_chart(datosF)
            
            st.write('Sentadilla')
            BestBF = powerlifting[powerlifting.Sex=='F']['BestSquatKg']
            st.line_chart(BestBF)
            
            st.write('Peso muerto')
            DeadkgF = powerlifting[powerlifting.Sex=='F']['BestDeadliftKg']
            st.line_chart(DeadkgF)
            
    else:
        kg_totales_hombres = str(round(sum(powerlifting['TotalKg'][powerlifting.Sex=='M']), ndigits=0))
        kg_totales_mujeres = str(round(sum(powerlifting['TotalKg'][powerlifting.Sex=='F']) , ndigits=0))
        st.write('El peso total levantado por hombres es de ' +  kg_totales_hombres + 'kg')
        st.write('El peso total levantado por mujeres es de ' +  kg_totales_mujeres + 'kg')






def set_equipamiento():
    st.subheader('¿El equipamiento influye en el resultado?')
    eq_peso_total = powerlifting.groupby(['Equipment'])['TotalKg'].sum()
    #como la mayotia de los deportistas usan Raw, lo mejor para comparar será usar la media y no el total
    eq_pesomedio_total = powerlifting.groupby(['Equipment'])['TotalKg'].mean()
    st.bar_chart(eq_pesomedio_total )
    st.write('A grandes rasgos vemos que influye poco. Sólo el equipamiento Multi-ply.')
    choice_tipo = st.selectbox('Elige  ejercicio:', ('Press de Banca', 'Sentadilla','Peso muerto'))
    
    if choice_tipo == 'Press de Banca':
        eq_pesomedio_press = powerlifting.groupby(['Equipment'])['BestBenchKg'].mean()
        st.bar_chart(eq_pesomedio_press)
    elif choice_tipo == 'Sentadilla':
        eq_pesomedio_sentadilla = powerlifting.groupby(['Equipment'])['BestSquatKg'].mean()
        st.bar_chart(eq_pesomedio_sentadilla)
    else:
        eq_pesomedio_pesomuerto = powerlifting.groupby(['Equipment'])['BestDeadliftKg'].mean()
        st.bar_chart(eq_pesomedio_pesomuerto)





        
        
        
        
        