"""
Ejercicio 2: Desarrolle un algoritmo que permita leer un valor cualquiera X y escribir si 
dicho número es par o impar.
"""
def ing_int(arg):
    return int(input(arg))

def p_Par_Impar():
    x = ing_int("Ingrese one numero entero:  ")
    if x % 2 ==0:
        print("El numero es par")
    else: print("El numero es impar")

p_Par_Impar()