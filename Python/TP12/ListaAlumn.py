"""
Manejo de la lista de alumnos
"""

from Mylibrary import *
from Alumnos import *

alumnos = {}

def askWTC(arg):
    x = ing_str(arg).upper()
    if x == 'Y':
        return True
    elif x == 'N':
        return False
    else:
        askWTC("Error, ingrese correctamente \n Ingrese Y/y o N/n: ")

def ing_alum():
    while True:
        dni = ing_int("Ingrese el DNI del alumno: ")
        nomb = ing_str("Ingrese el Nombre del alumno: ")
        apellido = ing_str("Ingrese el Apellido del alumno: ")
        telefono = ing_str("Ingrese el Telefono del alumno: ")
        correo = ing_str("Ingrese el Correo del alumno: ")

        alumnos[dni] = ini_alum(nomb,apellido,telefono,correo)
        if not askWTC("Desea seguir ingresando?\n Y/y para si\n N/n para no\n Ingrese Y/y o N/n: "):
            break

def elim_alumn(bus : int):
    try:
        del alumnos[bus]
    except:
        print("O nyo")

def show_alum(dnib : int):
    try:
        if alumnos[dnib]!= 'None':
            print("Dni: {dni}".format(dni = dnib))
            show(alumnos.get(dnib))
    except:
        print("No se encontro el alumno")

def show_all():
    for key, value in alumnos.items():
        print("Dni: {d}".format(d=key))
        show(value)

if __name__ == "__main__":
    ing_alum()
    show_all()