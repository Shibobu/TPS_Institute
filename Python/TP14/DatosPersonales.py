"""
Definir el diccionario de alumnos
"""
from random import *

def randNotas():
    return randint(1,10)

def inialum(dni,nombre,apellido,telefono,correo):
    alumno = {
        'DNI' : dni,
        'NOMBRE' : nombre,
        'APELLIDO' : apellido,
        'TELEFONO' : telefono,
        'CORREO' : correo,
        'NOTA' : randNotas()
        }
    return alumno

def show(alum):
        print("Nombre: {N}\n".format(N = alum["Nombre"]) +
          "Apellido: {A}\n".format(A = alum["Apellido"]) +
          "Nota del Parcial: {N}\n".format(N = alum["Nota"]))

def returnFields():
    return "DNI,NOMBRE,APELLIDO,TELEFONO,CORREO,NOTA"

def comp_exist(dni1,dni2):
    if dni1 < dni2:
        return 1
    if dni1 > dni2:
        return -1
    if dni1 == dni2:
        return 0