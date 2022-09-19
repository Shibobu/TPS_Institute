"""
Ejercicio 7: Desarrolle un algoritmo que permita leer un valor A y decir si dicho número 
es positivo, negativo o cero.
"""

def ing_float(arg):
    return float(input(arg))

def p_posneg0():
    A = ing_float("Ingrese un numero: ")
    
    if A == 0:
        print("El numero es Cero")
    elif A > 0:
        print("El numero es positivo")
    else: print("El numero es negativo")
    
p_posneg0()
