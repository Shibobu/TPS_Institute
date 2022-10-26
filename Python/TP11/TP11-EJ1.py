"""
Escribir una función que guarde en una variable el diccionario {‘Euro’:’€’, ‘Dólar’:’U$S’,
‘Yen’:’¥’,’Real’:’R$’} y luego pregunte al usuario por una divisa y muestre su símbolo o
un mensaje de aviso si la divisa no está en el diccionario.
"""

from Mylibrary import *

def p_Ejercicio1():
    divisas = {'Euro':'€', 'Dolar':'U$S','Yen':'¥','Real':'R$'}
    us = ing_str("Ingrese la divisa a comprobar su simbolo: ").title()
    try:
        print("El simbolo de la divisa {d} es {s}".format(d = us, s = divisas[us]))
    except:
        print("La divisa ingresada no se encuentra cargada")

if __name__ == "__main__":
    p_Ejercicio1()