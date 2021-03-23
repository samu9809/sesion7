contador = 1

while(contador <= 30):
    cont2 = 1
    potencia = 10
    while(cont2 < contador):
        potencia = potencia * 10
        cont2 = cont2 + 1
    print("10 a la " + str(contador) + " = " + str(potencia))
    contador = contador + 1