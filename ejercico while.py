print("Adivina el numero \n")
print("Pista, el numero no se pasa de 20")
numero = 8
usuario = 0

while usuario != numero:
    usuario = int(input("Cual es el numero: "))
    if usuario > numero:
        print("Digita un numero menor: ")
    elif usuario < numero:
        print("Digita un numero mayor: ")
    else: 
        print("Adivinaste el numero")