# Streamlit App

Streamlit es una herramienta para crear fácilmente aplicaciones web interactivas, desde Python. Muy similar a Shiny. En este caso, se ha utilizado la herramienta para crear una aplicación web que muestra unos datos referentes a una competición de powerlifting.


##  Obtención de los datos

Los datos provienen de **Kaggle**, una plataforma web que reúne la comunidad Data Science más grande del mundo, con más de 536 mil miembros activos en 194 países, recibe más de 150 mil publicaciones por mes, que brindan todas las herramientas y recursos más importantes para progresar al máximo en data science.

Me he descargado los datos a través de la API de Kaggle. Para ello, tienes que iniciar sesión y en tu perfil darle a account. Una vez allí, le das a ‘Create New API Token’, se descargará un archivo ‘kaggle.json’ en esta dirección ‘C: \Users\<username>\.kaggle\’.

#guardar tu token en la misma carpeta

#conectar con la Api de Kaggle

from kaggle.api.kaggle_api_extended import KaggleApi

api= KaggleApi()

api.authenticate()

Una vez aquí, buscamos el dataset : api.dataset_list_files('dansbecker/powerlifting-database').files

Creamos el directorio, y, nos descargamos los datos.

Después de todo esto utilizo una función para descomprimir el archivo y así obtengo las 2 bases de datos. (La descarga de estos datos se lleva a cabo en el archivo **script_datos_api_kaggle.py**).

## Preprocesamiento de datos

A la hora de la limpieza de datos, se realiza una limpieza básica. A los valores negativos se les pone valor 0 y el resto de Na´s se omiten. Luego se utiliza un filtro para los valores 0 que no tienen sentido (como la edad) y se guardan las bases de datos limpias en nuevos archivos csv.  
( Archivo **preparacion_datos.py**)

## Dashboard

Respecto al Dashborad, en la primera página se muestran los datos correspondientes, así como unos descriptivos de los mismos para poner en contexto los datos que se van a emplear, pudiendo elegir entre unos datos u otros.
Ya sea de las competiciones o de los concursantes.

En la segunda página se muestra la participación de las federaciones, así como los países, estados y ciudades en los que más encuentros o competiciones se realizan.

En la tercera página se analiza a los participantes, así como la edad y el peso que levantan según ejercicio o género.

Y, la última página, trata de descubrir si influye el equipamiento a la hora de realizar los ejercicios, tanto de manera global como de manera individual cada ejercicio.  

Archivo **app_functions.py**.  

Archivo **VisDin.py**.
