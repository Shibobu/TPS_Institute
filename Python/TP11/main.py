"""
Funcion principal Trabajo Practico 11
"""

from TP11EJ1 import p_Ejercicio1
from TP11EJ2 import p_Ejercicio2
from TP11EJ3 import fecha
from Mylibrary import ing_int


def menu():
    print("---------Ingrese una opcion ---------\n" +
          "------1) Ejercicio 1\n" +
          "------2) Ejercicio 2\n" +
          "------3) Ejercicio 3\n" +
          "------4) Salir")
    return ing_int("Ingrese una opcion: ")

if __name__ == "__main__":
    while True:
        match menu():
            case 1:
                p_Ejercicio1()
            case 2:
                p_Ejercicio2()
            case 3:
                fecha()
            case 4:
                print("Salir")
                break
            case _:
                print("Ingrese correctamente los datos: ")