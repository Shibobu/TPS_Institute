"""
Ejercicio 1: Escribir un programa que permita ingresar la edad en años de una persona 
y luego mostrar “Sos mayor de edad” o “No sos mayor de edad” según la edad ingresada.
"""


def ing_int(arg):
    return int(input(arg))
    

def ingreso(arg):
    cons = ing_int(arg) 
    return cons if(0 <= cons <= 120) else ingreso("Datos erroneos, ingrese nuevamente: ")

def p_edad():
    edad = False
    while edad == False:
        edad = ingreso("Ingrese su edad: ")
    if edad >= 18:
        print("Sos mayor de edad")
    else : print("No sos mayor de edad")

p_edad()