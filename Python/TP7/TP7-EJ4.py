"""
Ejercicio 4: Escribir una función que almacene las asignaturas de un curso (por ejemplo, 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota 
que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final 
el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir
"""

def ing_int(arg):
    return int(input(arg))

def compNotas(arg):
    notas = ing_int(arg)
    return notas if(1 <= notas <= 10) else compNotas("Datos erroneos, ingrese nuevamente: ")

def pedirNotas(mat):
    i = 0
    while i < len(mat):
        nota = compNotas("Ingrese su nota de la materia " + mat[i] + ": ")
        if nota >= 6: 
            del mat[i]
        else:
            i+=1

def salida(mat):
    for i in range(len(mat)):
        print("Usted debe recursar", mat[i])


def p_elimApr():
    mat = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
    pedirNotas (mat)
    salida(mat)
p_elimApr()