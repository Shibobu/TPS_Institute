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


if __name__ == "__main__":
    ListaAlumnos.ing_alumn()
    ListaAlumnos.createCSV('calificaciones.csv','w')
