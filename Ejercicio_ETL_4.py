import pandas as pd

"""Buen dia estimado Docente, este archvio CSV lo tomo yo Francisco Javier Hernandez Correal
de mi trabajo, con el permiso de poder utilizarlo y siendo responsable de su uso."""

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

def filtrar_por_tipo_ingreso(df, tipos_de_ingreso):
    """
    Filtra el DataFrame por los tipos de ingreso deseados.
    """
    return df[df['TIPO INGRESO'].isin(tipos_de_ingreso)]

def organizar_por_tipo_ingreso(df):
    """
    Organiza el DataFrame por el campo 'TIPO INGRESO'.
    """
    return df.sort_values(by='TIPO INGRESO')

def guardar_en_excel(df, archivo_salida):
    """
    Guarda el DataFrame organizado en un nuevo archivo Excel.
    """
    df.to_excel(archivo_salida, index=False)
    
def main():
    # Ruta del archivo CSV
    archivo_csv = "C:\\Users\\J-far\\Documents\\python\\Reporte de Seguimiento Diario_Detalle Produccion POS_Tabla.csv"
    # Tipos de ingreso deseados
    tipos_de_ingreso = ['TRASLADO', 'TRASLADO_SAT', 'NUEVO']

    # Cargar los datos
    df = cargar_datos(archivo_csv)

    # Filtrar por tipos de ingreso
    df_filtrado = filtrar_por_tipo_ingreso(df, tipos_de_ingreso)

    # Organizar por tipo de ingreso
    df_organizado = organizar_por_tipo_ingreso(df_filtrado)

    # Guardar en un nuevo archivo Excel
    archivo_excel_salida = "C:\\Users\\J-far\\Documents\\python\\Reporte de Seguimiento Diario_Detalle Produccion POS_Tabla.xlsx"  
    guardar_en_excel(df_organizado, archivo_excel_salida)
    
    print(f"Proceso completado. Archivo Excel creado: {archivo_excel_salida}")

if __name__ == "__main__":
    main()
