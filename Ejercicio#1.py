# Ejercicoio numero 1

# Importamos una libreria
import math

# Area de declaracion de variables
base = 0
area = 0
perimetro = 0

# Entradas
base = int(input("Digite la base del triangulo: "))

# Proceso
def area_triangulo():
    if base > 0:
        area = math.sqrt(3)/4 * math.pow(base,2)
        print("El area del triangulo es igual: ", area)
    else:
        print("Error")
    
def perimetro_triangulo():
    if base > 0:
        perimetro = base + base + base
        print("El perimetro del triangulo es: ", perimetro)
    else:
        print("Error")
    
# Fin del proceso
area_triangulo()
perimetro_triangulo()
