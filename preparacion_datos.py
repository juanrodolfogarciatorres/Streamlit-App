# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:42:24 2022

@author: jgarcia
"""

import pandas as pd

#cargamos los datos
meets = pd.read_csv('meets.csv')
meets.head(10)

powerlifting = pd.read_csv('openpowerlifting.csv')
powerlifting.head(10)



##Preprocesado de datos 'openpowerlifting.csv'
#Detección valores nulos
(powerlifting.isna().sum()/powerlifting.shape[0])*100
powerlifting.drop(["Squat4Kg","Bench4Kg","Deadlift4Kg"], axis=1 ,inplace=True)
powerlifting.drop_duplicates(inplace=True)
powerlifting.describe()

#cambiamos los negativos por 0
powerlifting[powerlifting["BestSquatKg"]<0]=0
powerlifting[powerlifting["BestBenchKg"]<0]=0
powerlifting[powerlifting["BestDeadliftKg"]<0]=0

#eliminamos el resto de na
powerlifting = powerlifting.dropna()


##Preprocesado de datos 'meets.csv'
(meets.isna().sum()/meets.shape[0])*100
meets = meets.dropna()