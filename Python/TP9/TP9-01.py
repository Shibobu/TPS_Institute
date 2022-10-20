"""
Ejercicio 1: Escriba una función que solicite una contraseña (el texto de la contraseña no
es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.
"""

def contra(passw):
    arg = "Ingrese la contraseña: "
    while str(input(arg)) != passw:
        arg = "Ingrese la contraseña nuevamente: "
    print("Finalizado")

def ped_ingreso(arg):
    return str(input(arg))

def p_contra():
    passw = ped_ingreso("Ingrese la constraseña para establecer la cuenta: ")
    contra(passw)

p_contra()

