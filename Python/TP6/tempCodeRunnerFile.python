"""
Ejercicio 10: Escribir un algoritmo que lea los nombres y edades de dos personas e 
imprima cuál de ellas tiene más edad o si son de la misma edad.
"""

def ing_int(arg):
    edad = int(input(arg))
    if edad < 0 or edad > 120:
        print("Edad incorrecta, ingrese nuevamente")
        return False
    else: return edad

def ing_Cad(arg):
    return str(input(arg))

def comp_edad():
    edad = False
    while edad == False:
        edad = ing_int("Ingrese la edad: ")
    return edad

def salidaMay(edad,nomb):
    print("El mayor es",nomb,"con",edad,"años de edad")

def p_compedad():
    name1 = ing_Cad("Ingrese el nombre de la primera persona: ")
    edad1 = comp_edad()
    name2 = ing_Cad("Ingrese el nombre de la segunda persona: ")
    edad2 = comp_edad()
    
    if edad1 > edad2:
        salidaMay(edad1,name1)
    elif edad1 == edad2:
        print("Son de la misma edad")
    else: salidaMay(edad2,name2)

p_compedad()
