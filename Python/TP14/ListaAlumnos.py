from DatosPersonales import *
from Mylibrary import *

alumnos = []

def ing_alumn():
    while True:
        print("Ingrese el {p}º alumno a cargar: \n".format(p =len(alumnos) + 1))
        dni = ing_int("Ingrese el DNI del alumno: ")
        nomb = ing_str("Ingrese el Nombre del alumno: ")
        apellido = ing_str("Ingrese el Apellido del alumno: ")


        alumnos.append(inialum(dni,nomb,apellido))
        if len(alumnos)>= 10 and not askWTC("Desea seguir ingresando?\n Y/y para si\n N/n para no\n Ingrese Y/y o N/n: "):
            break
    
def show_alum(inx):
    print(show_alum(alumnos[inx]))