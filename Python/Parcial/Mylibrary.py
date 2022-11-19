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

def ing_str(arg):
    return str(input(arg))

def ing_floatpox(arg):
    x = ing_float(arg)
    return x if x >= 0 else ing_floatpox("No se aceptan datos negativos, ingrese nuevamente")

def ing_zero(arg):
    x = ing_float(arg)
    return x if x != 0 else ing_zero("El valor no puede ser Zero, Ingrese nuevamente: ")

def askWTC(arg):
    x = ing_str(arg).upper()
    if x == 'Y':
        return True
    elif x == 'N':
        return False
    else:
        askWTC("Error, ingrese correctamente \n Ingrese Y/y o N/n: ")