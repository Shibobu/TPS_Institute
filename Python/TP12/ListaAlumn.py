"""
Manejo de la lista de alumnos
"""

from Mylibrary import *
from Alumnos import *

alumnos = []

def askWTC():
    x = ing_str("Desea seguir ingresando?\n Y/y para si\n N/n para no\n Ingrese Y/y o N/n: ").upper
    return True if x == 'Y' else False

def ing_alum():
    while True:
        dni = ing_int("Ingrese el DNI del alumno: ")
        nomb = ing_str("Ingrese el Nombre del alumno: ")
        apellido = ing_str("Ingrese el Apellido del alumno: ")
        telefono = ing_str("Ingrese el Telefono del alumno: ")
        correo = ing_str("Ingrese el Correo del alumno: ")

        alumnos.append(ing_alum(dni,nomb,apellido,telefono,correo))

        if not askWTC():
            break

def elim_alumn():
    for e in alumnos: 
        if e.get('DNI')
        