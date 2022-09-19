"""
Ejercicio 1:
Escribir una función que pregunte el nombre del usuario en la consola y un 
número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas 
veces como el número introducido. (No debe usar ciclos)
"""
from math import trunc


def ingr_str(arg):
    return str(input(arg))

def salida_N(text:str,n:int):
    print((text +"\n")*n)

def p_ej1():
    txt,n = ingr_str("Ingrese su nombre seguido de un espacio y un numero entero: ").split()
    salida_N(txt,trunc(float(n)))

p_ej1()