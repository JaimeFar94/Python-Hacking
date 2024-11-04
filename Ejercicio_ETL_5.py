import pandas as pd
import matplotlib.pyplot as plt

"""En este ejercicio se tomaron los datos de una base de datos libre en la pagina: 
https://www.datos.gov.co/Salud-y-Protecci-n-Social/INFECCION-RESPIRATORIA-AGUDA-GRAVE-INUSITADA/hzhs-nf5h/about_data
en la cual se quiere sacar el porcentaje de menores de edad que han tenido infecciones respiratorias agudas graves inusitadas."""

"""#Integrantes:
#Angie Morales
#Javier Hernández
#Jaime Farfan
#Johan Castro
#William Andrés Salavarrieta"""

def cargar_datos(archivo_csv):
    """
    Carga los datos desde un archivo CSV usando pandas.
    """
    return pd.read_csv(archivo_csv)

def calcular_porcentaje_menores_de_edad(df):
    """
    Calcula el porcentaje de menores de edad en la columna 'EDAD'.
    """
    menores_de_edad = df[df['EDAD'] < 18]
    porcentaje_menores = len(menores_de_edad) / len(df) * 100
    return porcentaje_menores

def limpiar_organizar_datos(df):
    """
    Realiza la limpieza y organización de los datos.
    """
    # Puedes realizar más operaciones de limpieza y organización según sea necesario
    # En este ejemplo, simplemente se organiza por la columna 'EDAD'
    df_organizado = df.sort_values(by='EDAD')

    return df_organizado

def guardar_en_excel(df, archivo_salida):
    """
    Guarda el DataFrame en un nuevo archivo Excel.
    """
    df.to_excel(archivo_salida, index=False)

def generar_grafica(porcentaje_menores):
    """
    Genera una gráfica de barras del porcentaje de menores de edad.
    """
    plt.bar(['Menores de Edad', 'Mayores de Edad'], [porcentaje_menores, 100 - porcentaje_menores])
    plt.title('Porcentaje de Menores de Edad')
    plt.xlabel('Grupo de Edad')
    plt.ylabel('Porcentaje')
    plt.show()

def main():
    # Ruta del archivo CSV
    archivo_csv = "C:\\Users\\J-far\\Documents\\python\\INFECCION_RESPIRATORIA_AGUDA_GRAVE_INUSITADA.csv" # Reemplaza con la ruta correcta de tu archivo CSV

    # Cargar los datos
    df = cargar_datos(archivo_csv)

    # Calcular el porcentaje de menores de edad
    porcentaje_menores = calcular_porcentaje_menores_de_edad(df)
    print(f"Porcentaje de menores de edad: {porcentaje_menores:.2f}%")

    # Generar gráfica
    generar_grafica(porcentaje_menores)

    # Limpiar y organizar los datos
    df_organizado = limpiar_organizar_datos(df)

    # Guardar en un nuevo archivo Excel
    archivo_excel_salida = "C:\\Users\\J-far\\Documents\\python\\E R Informacion Organizada por EDAD.xlsx"  # Nombre del nuevo archivo Excel
    guardar_en_excel(df_organizado, archivo_excel_salida)

    print(f"Proceso completado. Archivo Excel creado: {archivo_excel_salida}")

if __name__ == "__main__":
    main()
