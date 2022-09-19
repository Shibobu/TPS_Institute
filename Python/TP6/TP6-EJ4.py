"""
Ejercicio 4: Escribir un algoritmo que permita calcular al valor absoluto de un número 
entero X.
"""

def ing_int(arg):
    return int(input(arg))

def p_absValue():
    X = ing_int("Ingrese un numero: ")
    if X >= 0:
        print("El valor absoluto es:",X)
    else: print("El valor absoluto es:",abs(X))

p_absValue()