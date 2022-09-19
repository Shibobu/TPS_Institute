"""
Ejercicio 10: Escribir un algoritmo que lea los nombres y edades de dos personas e 
imprima cuál de ellas tiene más edad o si son de la misma edad.
"""

def ing_int(arg):
    return int(input(arg))

def ing_Cad(arg):
    return str(input(arg))

def ingreso(arg):
    cons = ing_int(arg) 
    return cons if(0 <= cons <= 120) else ingreso("Datos erroneos, ingrese nuevamente: ")

def salidaMay(edad,nomb):
    print("El mayor es",nomb,"con",edad,"años de edad")

def p_compedad():
    name1 = ing_Cad("Ingrese el nombre de la primera persona: ")
    edad1 = ingreso("Edad: ")
    name2 = ing_Cad("Ingrese el nombre de la segunda persona: ")
    edad2 = ingreso("Edad: ")
    
    if edad1 > edad2:
        salidaMay(edad1,name1)
    elif edad1 == edad2:
        print("Son de la misma edad")
    else: salidaMay(edad2,name2)

p_compedad()
