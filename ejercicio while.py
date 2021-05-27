# Sucesion de Fibonacci

# Declaracion de variables
num_cero = 0
num_uno = 1

while num_uno <= 1597:
    print(num_cero, num_uno, end="")
    num_cero = num_cero + num_uno 
    num_uno = num_cero + num_uno 
    
print(" resultado")