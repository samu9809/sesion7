import random
total = 0
promedio = 0

mayor_positivo = 0
mayor_negativo = -60

for x in range(5):
    numero_aleatorio = random.randint(-50, 50)
    print("NUMERO ALEATORIO CALCULADO: " + str(numero_aleatorio))
    if numero_aleatorio < 0:
        if numero_aleatorio > mayor_negativo:
            mayor_negativo = numero_aleatorio
    else:
        if numero_aleatorio > mayor_positivo:
            mayor_positivo = numero_aleatorio
    
    total = total + numero_aleatorio
    print("total "+str(total))

promedio = total/100
print("SUMA:" + str(total))
print("PROMEDIO: " + str(promedio))
print("MAYOR POSITIVO:" + str(mayor_positivo))
print("MAYOR NEGATIVO:" + str(mayor_negativo))

############################################################

import random
total = 0
promedio = 0

mayor_positivo = 0
mayor_negativo = -60

contador = 0
while(contador <= 100):
    numero_aleatorio = random.randint(-50, 50)
    print("NUMERO ALEATORIO CALCULADO: " + str(numero_aleatorio))
    if numero_aleatorio < 0:
        if numero_aleatorio > mayor_negativo:
            mayor_negativo = numero_aleatorio
    else:
        if numero_aleatorio > mayor_positivo:
            mayor_positivo = numero_aleatorio
    
    total = total + numero_aleatorio
    print("total "+str(total))
    contador = contador + 1

promedio = total/100
print("SUMA:" + str(total))
print("PROMEDIO: " + str(promedio))
print("MAYOR POSITIVO:" + str(mayor_positivo))
print("MAYOR NEGATIVO:" + str(mayor_negativo))
