import pandas as pd 

try:
    # Intenta leer el archivo con punto y coma como delimitador y utf-8 como codificación
    df = pd.read_csv('C:/Users/J-far/Documents/python/datos.csv', delimiter=';', encoding='utf-8') 
except UnicodeDecodeError:
    # Si hay un error de decodificación, intenta leer con latin1 como codificación
    df = pd.read_csv('C:/Users/J-far/Documents/python/datos.csv', delimiter=';', encoding='latin1')
 

df.isnull #permite detectar datos nulos
df.notnull #Es la indicación lógica contraria, y la forma de llamar a la función es similar.

#Limpieza de datos

#df.dropna() que se encarga de eliminar los datos nulos
#df.fillna(Value = 100) se enccarga de reemplazar los valores nulos.

print(df.shape) # Obtener la forma de la hoja de cálculo.


print(df.columns)# Obtener los nombres de las columnas de la hoja de cálculo.


print(df.describe()) #da un resumen de la tabla

df.drop_duplicates(inplace=True) #Elimina las Filas duplicadas 
df.columns = df.columns.str.strip() #Eliminar los espacios que se encuentran entra las columnas


#Analisis de información 

#EL producto mas solicitado
tp_product = df['Tipo de producto'].value_counts()
print("El producto mas Solicitado es:\n", tp_product)

#Importe de costo total mas alto y bajo

Impo_cost = df['Importe Coste total'].max
print("El importe de costo toral mas alto es:\n",Impo_cost)
Impo_costa = df['Importe Coste total'].min
print("El importe minimo es:\n",Impo_costa)

#Promedio de Importe venta total
df['Importe venta total'] = pd.to_numeric(df['Importe venta total'], errors='coerce') #Convierte las columnas relevantes a números
df = df.dropna(subset=['Importe venta total']) #Este método se utiliza para eliminar filas que contienen valores nulos (NaN) en el DataFrame.
Impo_vent = df['Importe venta total'].mean() #Calcula el valor promedio de los elementos en la columna seleccionada
print("El promedio de Importe venta total es:\n",Impo_vent)


#Exportar información
tp_product.to_excel("C:/Users/J-far/Documents/python/tp_product.xlsx") #se indica la ruta donde quiere ser almacenada la información

