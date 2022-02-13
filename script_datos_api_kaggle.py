# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 12:28:34 2022

@author: jgarcia
"""

import kaggle
import pandas as pd
import os
from zipfile import ZipFile
import pandas as pd

#guardar tu token en la misma carpeta (la que te indica al importar kaggle)

#conectar con la Api de Kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api= KaggleApi()
api.authenticate()

#buscar el dataset
api.dataset_list(search='powerlifting', file_type='csv')

#Al elegir el dataset ver que contiene
api.dataset_list_files('dansbecker/powerlifting-database').files

#crear directorio
path= os.getcwd() + '/datos_powerlifting'

#indicar si ha sido creado correctamente el directorio
try:
    os.mkdir(path)
except OSError:
    print('creación fallida')
else:
    print('Ha sido creado con éxito' )


#cambiar barra de un lado a otro
api.dataset_download_files('dansbecker/powerlifting-database',
                           '/Users/jgarcia/.kaggle/datos_powerlifting')

#Descomprimir archivo zip
def descomprimir():
    archivozip='C:\\Users\\jgarcia\\.kaggle\\datos_powerlifting\\powerlifting-database.zip'
    
    with ZipFile (file = archivozip, mode= 'r' , allowZip64= True) as file:
        archivo = file.open(name= file.namelist()[0], mode= 'r')
        print(archivo.read())
        archivo.close()
        
        navegacion='C:\\Users\\jgarcia\\.kaggle\\datos_powerlifting'
        print('Descomprimiendo archivos') 
        file.extractall(path=navegacion)
        print('Archivo descomprimido')
        
descomprimir()


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
power_clean = powerlifting.dropna()


##Preprocesado de datos 'meets.csv'
(meets.isna().sum()/meets.shape[0])*100
meets_clean = meets.dropna()

#guardo los datos que ya puedo usar directamente para la parte de visualización
power_clean.to_csv('.\\power_clean.csv', index = False)
meets_clean.to_csv('.\\meets_clean.csv', index = False)

