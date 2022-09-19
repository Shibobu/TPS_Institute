"""
Ejercicio 17: Escribir un programa que almacene una contraseña en una variable de tipo 
de cadena de caracteres, pregunte al usuario por la contraseña e imprima por pantalla 
si la contraseña introducida por el usuario coincide con la guardada en la variable 
teniendo en cuenta mayúsculas y minúsculas.
"""

def ing_cad(arg):
    return str(input(arg))

def p_password():
    pasword = "AsgatiopIalomIzona"

    print("Pista: la contraseña tene",pasword.__len__(),"letras")
    pasTry = ing_cad("Ingrese la contraseña para ingresar: ")
    
    if(pasTry == pasword):
        print("Contraseña correcta, bienvenido")
    else: print("Contraseña incorrecta, alertando a las autoridades")

p_password()