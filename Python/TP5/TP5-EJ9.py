"""
Ejercicio 9:
Escribir una función que pregunte por consola por los productos de un carrito 
de compras, separados por comas, y muestre por pantalla cada uno de los productos en 
una línea distinta.
"""

def ingr_str(arg):
    return str(input(arg))

def salida(arg):
    print(arg)

def p_ej9():
    carrito = ingr_str("Ingrese los productos del carrito,"
                    +" separando cada item con una coma:\n").replace(",","\n")
    salida(carrito)

p_ej9()