# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:45:37 2021

@author: samuel marin h.
"""
print("Sistema de notas de un curso de programacion")

#Entrada

numeroEstudiantes=int(input("Digite la cantidad de estudiantes del grupo : "))

# Declarar la variable que controla el ciclo
contadorRepeticiones=0 
cantidadEstudiantesAprobaron=0
cantidadEstudiantesReprobaron=0 
sumaDefinitivaEstudiantes=0
sumaDefinitivaEstudiantesAprobaron=0.0
sumaDefinitivaEstudiantesReprobaron=0.0
promedioDefinitivaEstudiantes=0.0
promedioDefinitivaEstudiantesAprobaron=0.0
promedioDefinitivaEstudiantesReprobaron=0.0
maximaNotaDefinitivaEstudiantesAprobaron=0.0
minimaNotaDefinitivaEstudiantesReprobaron=0.0
#Proceso
# Iniciar el ciclo

while contadorRepeticiones < numeroEstudiantes:
    # Lectura de las notas de cada estudiante
    nombreEstudiante = (input("Digite nombre del estudiante : "))
    notaUnoEstudiante = float(input("Digite la nota del primer parcial del estudiante : "))
    notaDosEstudiante = float(input("digite la nota del segundo parcial del estudiante : "))    
    notaTresEstudiante = float(input("digite la nota del tercer parcial del estudiante : "))   
    # Calcular la definitiva de cada estudiante  
    notaDefinitiva = (notaUnoEstudiante+notaDosEstudiante+notaTresEstudiante)/3
    #sumar las definitivas de los estudiantes para calcular el promedio
    sumaDefinitivaEstudiantes=sumaDefinitivaEstudiantes+notaDefinitiva
    print("1. La definitiva es : ", notaDefinitiva)
    
    if(notaDefinitiva>=3.0):
        cantidadEstudiantesAprobaron=cantidadEstudiantesAprobaron+1
        # Sumar las notas de los estudiantes que aprobaron
        sumaDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron+notaDefinitiva
    else:
        cantidadEstudiantesReprobaron=cantidadEstudiantesReprobaron+1
        # Sumar las notas de los estudiantes que reprobaron
        sumaDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron+notaDefinitiva
    # Incrementar la variable que controla el ciclo
    contadorRepeticiones = contadorRepeticiones+1
    
    # fin del ciclo
# Calcular el promedio del grupo    
promedioDefinitivasEstudiantes=sumaDefinitivaEstudiantes/numeroEstudiantes

if (cantidadEstudiantesAprobaron>0):
    promedioDefinitivaEstudiantesAprobaron=sumaDefinitivaEstudiantesAprobaron/cantidadEstudiantesAprobaron
if (cantidadEstudiantesReprobaron>0):
    promedioDefinitivaEstudiantesReprobaron=sumaDefinitivaEstudiantesReprobaron/cantidadEstudiantesReprobaron

print("Otros calculos")
print("2. Cantidad de estudiantes que aprobaron : ", cantidadEstudiantesAprobaron)
print("3. Cantidad de estudiantes que reprobaron : ", cantidadEstudiantesReprobaron)
print(f"4. Promedio del grupo : {promedioDefinitivaEstudiantes : .2f}")
print("5. Promedio de estudiantes que aprobaron : ", promedioDefinitivaEstudiantesAprobaron)
print(f"6. Promedio de estudiantes que Reprobaron : , {promedioDefinitivaEstudiantesReprobaron : .1f}")
print("7. Maxima nota de estudiantes que aprobaron : ", maximaNotaDefinitivaEstudiantesAprobaron)
print("8. Minima nota de estudiantes que reprobaron : ", minimaNotaDefinitivaEstudiantesReprobaron)
    
      
   
