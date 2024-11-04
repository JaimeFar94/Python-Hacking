import pandas as pd

df = pd.read_csv('C:/Users/J-far/Documents/python/bestsellers.csv') #se indica la ruta del archivo como adicionalmente se procede a llamar a df

df.isnull #permite detectar datos nulos
df.notnull #Es la indicación lógica contraria, y la forma de llamar a la función es similar.

print(df.head()) #Obtener las primeras 5 filas de la hoja de cálculo


print(df.shape) # Obtener la forma de la hoja de cálculo.


print(df.columns)# Obtener los nombres de las columnas de la hoja de cálculo.


print(df.describe()) #da un resumen de la tabla



df.drop_duplicates(inplace=True) #Elimina las Filas duplicadas 

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True) #se renombra las columnas de las tablas


#Analizando por popularidad del autor

author_counts = df['Author'].value_counts() #Se procede a crear una variable nueva como tambien se selecciona la columna de autores y contara los autores al momento de imprimir.
print("Los autores mas populares son:\n", author_counts)


#Analizando por genero

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print("La clasificación por genero es :\n", avg_rating_by_genre)

#Analizando por precio mas alto

df['Price'] = pd.to_numeric(df['Price'], errors='coerce') #Convierte las columnas relevantes a números

# Encuentra el precio más alto
max_price = df['Price'].max()

print("El precio mas alto es: \n ", max_price)






