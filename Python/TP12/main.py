"""
principal
"""

from turtle import pen
from Mylibrary import ing_int
from ListaAlumn import *


def menu():
    print("Ingrese una Opcion:\n" +
          "1) Ingresar un alumno\n" +
          "2) Borrar un alumno\n" +
          "3) Mostrar un alumno\n" +
          "4) Mostrar todos los alumnos\n" +
          "5) Salir")
    return ing_int("Ingrese una Opcion: ")

if __name__ == "__main__":
    while True:
        match menu():
            case 1:
                ing_alum()
            case 2:
                dni = ing_int("Ingrese el dni a eliminar: ")
                elim_alumn(dni)
            case 3:
                dni = ing_int("Ingrese el dni del alumno a mostrar: ")
                show_alum(dni)
            case 4:
                show_all()
            case 5:
                print("Salir")
                break
            case _:
                print("Opcion seleccionada inexistente, ingrese nuevamente: ")