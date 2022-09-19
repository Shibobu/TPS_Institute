"""
Ejercicio 2:
Escribir una función que pida una cadena y un carácter por teclado y muestra 
cuantas veces aparece el carácter en la cadena.
"""

def ingr_str(arg):
    return str(input(arg))

def sal_charTimes(txt:str, c:str):
    print("En el texto: ", txt,
        "aparece " ,txt.count(c),
        " veces el caracter \"{c}\"".format(c=c))

def salida(arg):
    print(arg)

def p_Ej2():
    txt = ingr_str("Ingrese un mensaje: ")
    c = ingr_str("Ingrese un caracter: ")
    if c.__len__() > 1:
        salida("ERROR, NO INGRESO UN CARACTER, SI NO UNA CADENA")
    else:
        sal_charTimes(txt,c)

p_Ej2()