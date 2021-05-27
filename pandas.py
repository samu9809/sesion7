# Lectura de archivos tipo excel
# Importar librerias
import pandas as pd

# Leer archivo excel
archivo_excel = pd.read_excel('ventas.xLsx')

# Imprimir los datos
print(archivo_excel)