"""Ejercicio 7:
Escribir una función que pregunte el correo electrónico del usuario en la 
consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte 
delante de la arroba @) pero con dominio edu.ar
"""
def ingr_str(arg):
    return str(input(arg))

def salida(arg):
    print(arg)

def p_Ej7():
    mail,dom= ingr_str("Ingrese su correo electronico: ").split('@')
    dom = ".edu.ar"
    salida(mail + dom)

p_Ej7()