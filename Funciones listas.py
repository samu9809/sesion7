# Ordenamiento Burbuja
# Definicion del vector


lista_enteros = [5,20,3,4,9,43,2,45,24,85]

# Funcion que realiza el ordenamiento Burbuja

def ordBurbuja (lista_desordenada):
    for n in range (1,len(lista_desordenada)-1):
        for i in range (0,len(lista_desordenada)-1):
            if lista_desordenada[i] > lista_desordenada[i+1]:
                aux = lista_desordenada[i]
                lista_desordenada[i] = lista_desordenada[i+1]
                lista_desordenada[i+1] = aux
    print(lista_enteros)
                
# Fin del ordenamiento
# Llamar la funcion ordenar Burbuja

ordBurbuja(lista_enteros)