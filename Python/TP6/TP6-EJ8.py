"""
Ejercicio 8: Desarrolle un algoritmo que permita leer tres valores distintos A, B y C y 
luego indique el menor de ellos.
"""
def ing_int(arg):
    return int(input(arg))

def p_menor():
    A = ing_int("Ingrese un numero: ")
    B = ing_int("Ingrese otro numero: ")
    C = ing_int("Ingrese otro numero: ")
    
    men = A
    if B < men: 
        men = B
    if C < men:
        men = C

    print("El menor de los numeros es:",men)

p_menor()