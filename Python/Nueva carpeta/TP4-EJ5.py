"""
Ejercicio 5:
Desarrolle un programa que permita determinar la hipotenusa de un 
triángulo rectángulo conocidas las longitudes de sus dos catetos.
"""

import math

def ingr(arg):
    return int(input(arg))

def hipot():
    cat1 = ingr("Ingrese el primer cateto: ")
    cat2 = ingr("Ingrese el segundo cateto: ")
    hip = math.sqrt(pow(cat1,2)+pow(cat2,2))
    salida("El resultado es: " + str(hip))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    hipot()
