"""
Ejercicio 3: Desarrolle un algoritmo que permita leer un valor cualquiera A y escribir si 
dicho número es múltiplo de Z.
"""
def ing_int(arg):
    return int(input(arg))

def p_Multiplo():
    A = ing_int("Ingrese un numero: ")
    Z = ing_int("Ingrese un numero a comparar multiplo: ")

    if A % Z == 0:
        print("El numero",A, "es multiplo de",Z)
    else :  print("El numero",A, "no es multiplo de",Z)

p_Multiplo()