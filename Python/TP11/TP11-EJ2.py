"""
Escribir una función que pregunte al usuario su nombre, edad, dirección y teléfono y lo
guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

from Mylibrary import *


def p_Ejercicio2():
    persona = {}
    persona["nombre"] = ing_str("Ingrese el Nombre completo de la persona: ")
    persona["edad"] = ing_int("Ingrese la edad de la persona: ")
    persona["direccion"] = ing_str("Ingrese la direccion de la persona: ")
    persona["telefono"] = ing_str("Ingrese el telefono de la persona: ")

    print("{n} tiene {e} años, vive en {d} y su numero de telefono es: {t}".format(
        n = persona["nombre"],
        e = persona["edad"],
        d = persona["direccion"],
        t = persona["telefono"]))

if __name__ == "__main__":
    p_Ejercicio2()