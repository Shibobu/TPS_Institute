"""
Definir el diccionario de alumnos
"""
from random import *

def randNotas():
    return randint(1,10)

def inialum(dni,nombre,apellido):
    alumno = {
        'DNI' : dni,
        'Nombre' : nombre,
        'Apellido' : apellido,
        'Nota' : randNotas()
        }
    return alumno

def show(alum):
        print("Nombre: {N}\n".format(N = alum["Nombre"]) +
          "Apellido: {A}\n".format(A = alum["Apellido"]) +
          "Nota del Parcial: {N}\n".format(N = alum["Nota"]))
