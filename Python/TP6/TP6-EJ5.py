"""
Ejercicio 5: Desarrolle un algoritmo que permita leer dos valores A y B y que escriba cuál 
es el mayor.
"""

def ing_int(arg):
    return int(input(arg))

def p_mayor():
    A = ing_int("Ingrese un numero: ")
    B = ing_int("Ingrese otro numero: ")

    if A > B:
        print("El mayor es",A)
    elif B > A:
        print("El mayor es",B)

p_mayor()