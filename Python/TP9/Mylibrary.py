"""
Toma los modulos mas comunes para resolver el problema
"""

from math import trunc


def ing_int(arg:str):
    try:
        x = int(input(arg))
        return x
    except:
        print("Error de ingreso, Dato Erroneo")
        return ing_int("Ingrese nuevamente: ")

def ing_float(arg:str):
    try:
        x = float(input(arg))
        return x
    except:
        print("Error de ingreso, Dato Erroneo")
        return ing_int("Ingrese nuevamente: ")
