"""
Ejercicio 1:
Crear un script que lea los datos de un archivo de texto del tipo .csv con al menos 5 filas 
con la misma estructura del Trabajo Práctico Nro.12 (DNI, nombre, dirección, teléfono, 
correo electrónico); cabe destacar que al mostrar los datos deberán estar con su 
correspondiente nombre de columna
Ejemplo:
DNI:26452458, Nombre: Jesús González, Dirección: Alvarado 850, Teléfono:
387585698, Correo Electrónico: ingjesusgonzalez@yahoo.com.ar
DNI:3659874, Nombre:………….., Dirección:…………..
"""
import csv

def opCSV(filename, mode):
    with open(filename,mode) as csvFile:

        entrada = list(csv.DictReader(csvFile,delimiter= ';'))

    csvFile.close()
    return entrada

def showCSV(ls):
    cNames = get_colNames().split(',')
    for i in ls:
        for j in cNames:
            print(j, ":",i[j],"\n",end= " ")
        print(" ")

def get_colNames():
    
    return "DNI,NOMBRE,APELLIDO,DIRECCION,TELEFONO,CORREO ELECTRONICO"

if __name__ == "__main__":
    ls = opCSV('TP13\\a.csv','r')
    showCSV(ls)

    