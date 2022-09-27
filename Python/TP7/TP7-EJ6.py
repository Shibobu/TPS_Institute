"""
Ejercicio 6: Realizar una función que cree una lista e inicializarla con 5 cadenas de 
caracteres leídas por teclado. Copia los elementos de la lista en otra lista, pero en orden 
inverso, y muestra sus elementos por la pantalla.
"""
from audioop import reverse


def ing_str(arg):
    return str(input(arg))

def salida(list):
    for i in list:
        print(i)

def p_lista():
    list1 = []
    list2 = []
    for i in range(5):
        list1.append(ing_str("Ingrese una cadena de caracteres: "))
    list2 = list1.copy()
    list2.reverse()
    salida(list2)

p_lista()