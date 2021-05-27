# Ejercicio numero 2

# Importamos una libreria para poder utilizar la funcion sqrt
import math

# Area de declaracion de variables
A = 0
B = 0
C = 0
S = 0

# Entradas 
A = int(input("Digite A: "))
B = int(input("Digite B: "))
C = int(input("Digite C: "))

# Proceso
def area_triangulo():
    if A > 0 and B > 0 and C > 0:
        S = (A + B + C)/2
        area = math.sqrt(S * (S - A) * (S - B) * (S - C))
        print("El aera del triangulo es: ", area)
    else:
        print("Debe ser mayor que cero")
    
def perimetro_triangulo():
    if A > 0 and B > 0 and C > 0:
        perimetro = A + B + C
        print("El perimetro del triangulo es: ", perimetro)
    else:
        print("Debe ser mayor a cero")
    
# Fin del proceso
area_triangulo()
perimetro_triangulo()