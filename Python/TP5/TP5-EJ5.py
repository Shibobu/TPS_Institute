"""
Ejercicio 5:
Escribir una función que pida al usuario que introduzca una frase en la 
consola y muestre por pantalla la frase invertida.
"""

def ingr_str(arg):
    return str(input(arg))

def sal_Inv(txt:str):
    print(txt[::-1])

def p_ej5():
    txt = ingr_str("Ingrese una frase: ")
    sal_Inv(txt)

p_ej5()