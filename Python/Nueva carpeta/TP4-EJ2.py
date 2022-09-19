"""
Ejercicio 2:
Escribir un programa que permita ingresar al año de nacimiento de una 
persona y luego calcule su edad.
"""

import datetime
def ingr(arg):
    return int(input(arg))

def edad():
    b = True

    while b:
        anioNac = ingr("Ingrese su año de nacimiento: ")
        today = datetime.datetime.now().year
        
        if anioNac > today :
            salida("Si claro viajero del futuro, volve a ingresar")

        elif anioNac < 1890:
            salida("Deberia estar muerto, ¿Acaso eres inmortal?") 

        else:
             b=False
    salida("Su edad es: "+ str(today-anioNac))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    edad()
