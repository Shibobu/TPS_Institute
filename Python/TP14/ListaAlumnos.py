from DatosPersonales import *
from Mylibrary import *
import csv

alumnos = []

def ing_alumn():
    while True:
        print("Ingrese el {p}º alumno a cargar: \n".format(p =len(alumnos) + 1))
        dni = ing_int("Ingrese el DNI del alumno: ")
        nomb = ing_str("Ingrese el Nombre del alumno: ")
        apellido = ing_str("Ingrese el Apellido del alumno: ")
        telefono = ing_str("Ingrese numero de telefono: ")
        correo = ing_str("Ingrese correo: ")

        alumnos.append(inialum(dni,nomb,apellido,telefono,correo))
        if len(alumnos)>= 10 and not askWTC("Desea seguir ingresando?\n Y/y para si\n N/n para no\n Ingrese Y/y o N/n: "):
            break
    

def createCSV(filename,state):

    with open(filename,state) as file:

        fieldnames = returnFields().split(',')
        archive = csv.DictWriter(file,fieldnames=fieldnames)

        archive.writeheader()

        archive.writerows(alumnos)
    file.close()

def openCSV(filename,state):
    
    with open(filename,state) as file:

        ent = list(csv.DictReader(file,delimiter=','))
    file.close()

    return ent