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
    
def show_alum(inx):
    print(show_alum(alumnos[inx]))

def createCSV(filename,state):

    with open(filename,state) as file:

        fieldnames = returnFields().split(',')
        archive = csv.DictWriter(file,fieldnames=fieldnames)

        archive.writeheader()

        archive.writerows(alumnos)

def confExist(dni):
    ini = 0
    fin = len(alumnos)
    m = (ini + fin)/2
    while ini < fin & comp_exist(alumnos[m]['DNI'],dni) != 0:
        if comp_exist(alumnos[m]['DNI'],dni) > 0:
            ini = m+1
        if comp_exist(alumnos[m]['DNI'],dni) < 0:
            fin = m-1
    
    return m if ini < fin else -1

