"""
Ejercicio 3: 
Escribir una función que pregunte el nombre completo del usuario en la 
consola y después muestre por pantalla el nombre completo del usuario tres veces, una 
con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la 
primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir 
su nombre combinando mayúsculas y minúsculas como quiera.
"""

def ingr_str(arg):
    return str(input(arg))

def minusculas(arg:str):
    return arg.lower()

def mayusculas(arg:str):
    return arg.upper()

def titulo(arg:str):
    return arg.title()

def salida(arg):
    print(arg)

def p_ej3():
    nomb = ingr_str("Ingrese su nombre completo: ")
    nomb = minusculas(nomb)
    salida(nomb)
    salida(mayusculas(nomb))
    salida(titulo(nomb))
    
p_ej3()
