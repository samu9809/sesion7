# Conjucion and
num_uno = int(input("Escribe un numero mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("EL numero ", num_uno, "cumple con la condicion")
else:
    print("El numero ", num_uno, "no cumple con la condicion")
    
# Disyuncion or 
palabra = input("Para cumplir con la condicion escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condicion se ha cumplido")
else:
    print("La condicion no se ha cumplido")
    
# Negacion not
num_uno = int(input("Introduce un numero igual a 5: "))

if not num_uno == 5:
    print("El numero es diferente de 5 y si cumple la condicion")
else:
    print("El numero es igual a 5 y no cumple la condicion")