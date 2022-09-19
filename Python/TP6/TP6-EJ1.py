"""
Ejercicio 1: Escribir un programa que permita ingresar la edad en años de una persona 
y luego mostrar “Sos mayor de edad” o “No sos mayor de edad” según la edad ingresada.
"""


def ing_edad(arg):
    edad = int(input(arg))
    if edad < 0 or edad > 120:
        print("Edad incorrecta, ingrese nuevamente")
        return False
    else: return edad

def p_edad():
    edad = False
    while edad == False:
        edad = ing_edad("Ingrese su edad: ")
    if edad > 18:
        print("Sos mayor de edad")
    else : print("No sos mayor de edad")

p_edad()