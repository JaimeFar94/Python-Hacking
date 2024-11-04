import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/J-far/Documents/python/Alzheimer_s_Disease_and_Healthy_Aging_Data.csv')


#Limpieza de Datos como se ve dentro de este archivo se evidencia que tiene datos NaN por lo cual se procede a se reemplazados

#df.dropna(thresh=2) #elimina las filas que tengas 2 o mas valores NaN



df = df.fillna(method="bfill") #Este método rellena los datos nulos, en base al valor de la siguiente fila.


print(df.shape) # Obtener la forma de la hoja de cálculo.


print(df.columns)# Obtener los nombres de las columnas de la hoja de cálculo.


print(df.describe()) #da un resumen de la tabla

df.drop_duplicates(inplace=True) #Elimina las Filas duplicadas 


#analisis de información

#Evolución de YearStart
df['YearStart'] = pd.to_numeric(df['YearStart'], errors='coerce') #se procede a convertir la columna a tipo númerico

# Filtra las filas que no tengan NaN en la columna 'YearStart'
df_filtered = df.dropna(subset=['YearStart'])

# Crea el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(df_filtered['YearStart'], marker='o', linestyle='-')

# Añade etiquetas y título al gráfico
plt.xlabel('Índice de Filas')
plt.ylabel('Año de Inicio')
plt.title('Evolución de YearStart a lo largo del tiempo')

# Muestra el gráfico
plt.show()

print(df)