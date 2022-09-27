"""
Ejercicio 5: Realizar una función que inicialice una lista con 10 valores aleatorios (del 1 
al 10) y posteriormente muestre en pantalla cada elemento de la lista junto con su 
cuadrado y su cubo.
"""

from random import randint, seed

def salCuadCub(num):
    for i in num:
        print("Numero:",i,"\tCuadrado:",pow(i,2),"\tCubo:",pow(i,3))

def p_fillRand():
    seed()
    num = []
    for i in range(10):
        num.append(randint(1,10))
    salCuadCub(num)

p_fillRand()    