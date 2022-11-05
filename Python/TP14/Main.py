"""
Programar un script que pueda crear a partir de una lista o diccionario (como ud. lo 
prefiera); un archivo llamado calificaciones.csv el cual contiene los datos personales y 
las notas del Primer Parcial de al menos 10 (diez) alumnos de la materia Programación 
II del ISDeM (utilizar las mismas columnas del Trabajo Práctico Nro.13 agregando una 
columna para la nota que deberá ser un número aleatorio entre 1 y 10).
Construir una función que lea el archivo calificaciones.csv y devuelva un diccionario con 
los datos del archivo por columnas.
Construir una función que reciba el diccionario devuelto por la función anterior y cree 
un archivo en formato txt denominado resumen.txt en donde deberá decir en la primera 
línea “Resumen de Notas Primer Parcial Programación II”, además de los resultados de 
la mínima, la máxima y el promedio de notas de todos los alumnos.
"""

import ListaAlumnos

def prom(suma,cant):
    return suma / cant

def writeTXT(filename, state):

    with open(filename,state)as file:
        
        file.write("Resumen Notas Primer Parcial Programacion II: \n")
        file.write(str_Conv())
        file.write("\nMinima : " + str(m))
        file.write("\nMaxima : " + str(M))
        file.write("\nPromedio de las notas de todos los alumnos: " + str(prom(sum,len(ent))))
        print("Creaccion Completada!")
    file.close()

def str_Conv():
    aux = ListaAlumnos.returnFields().split(',')
    k = 1
    reV1 = " "
    for i in ent:
        reV1 += "\n{ka}º Alumno: \n".format(ka = k)
        k+=1
        for j in aux:
                reV1 +=(j + " : "+ i[j] +"\n")
        reV1 += " "
    return reV1

if __name__ == "__main__":
    ListaAlumnos.ing_alumn()
    ListaAlumnos.createCSV('TP14\src\\calificaciones.csv','w')
    ent = ListaAlumnos.openCSV('TP14\src\\calificaciones.csv','r')
    sum = 0 
    m = 0 

    for i in ent:
        ax = int(i['NOTA'])
        sum += ax
        if not m:
            m = ax
            M = ax
        if ax < m: m = ax
        if ax > M: M = ax
    
    writeTXT("TP14\src\\resumen.txt",'w')
