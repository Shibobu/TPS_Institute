"""
Escribir un programa que permita gestionar la base de datos de alumnos
del ISDeM. Los alumnos se guardaran en una lista o diccionario
desde python (lo que ud. prefiera) separados por comas con el 
siguiente contenido: DNI, nombre y apellido, direccion, telefono,
correo electronico, nota_parcial.

El programa debe preguntar al usuario por una opcion del siguiente
menú:
(1) Generar CSV
    -Crear generador de Contenido
(2) Leer CSV y mostrar contenido
(3) Exportar el promedio de notas en un archivo de texto
(4) Mostrar la mayor nota
(5) Mostrar la menor nota
(6) Salir
"""
from CSVManager import *
from ListAlumnos import *
from time import sleep

def menu():
    print("Ingrese una opcion:\n"
        +   "1) Crear un CSV\n"
        +   "2) Leer un CSV\n"
        +   "3) Exportar el promedio de notas\n"
        +   "4) Mostrar la mayor nota\n"
        +   "5) Mostrar la menor nota\n"
        +   "6) Salir\n")
    return ing_int("Ingrese una opcion: ")

def promnotas(alumn):
    sum = 0
    for i in alumn:
        sum += i['Nota_Parcial']
    return sum /len(alumn)

def maynot(alum):
    B= 0
    for i in alum:
        aux = i['Nota_Parcial']
        if not B:
            may = aux
            B = 1
        if may < aux:
            may = aux
    print("La mayor nota es:", may)

def mennot(alum):
    B= 0
    for i in alum:
        aux = i['Nota_Parcial']
        if not B:
            men = aux
            B = 1
        if men > aux:
            men = aux
    print("La menor nota es:", men)

if __name__ == "__main__":
    alumnos = []
    regAlumn(alumnos)
    fields = "DNI,Nombre,Apellido,Direccion,Telefono,Correo_Electronico,Nota_Parcial"
    b = 0
    while True:
        match(menu()):
            case 1:
                
                b = generateCSV('AlumnosISDeM.csv','w',alumnos,fields)
                print("Generada!")
                sleep(0.6)

                #Crear CSV
            case 2:
                if b:
                    ent = showALL('AlumnosISDeM.csv', 'r')
                sleep(0.6)
                #Leer CSV
            case 3:
                writeTXT('Promedio.TXT','w',promnotas(alumnos))
                sleep(0.6)
            case 4:
                maynot(alumnos)
                sleep(0.6)
            case 5:
                mennot(alumnos)
                sleep(0.6)
            case 6:
                #Salir
                print("Salir")
                break
            case _:
                print("Opcion ingresada inexistente, ingrese nuevamente: ")