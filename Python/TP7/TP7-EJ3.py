"""
Ejercicio 3: Escribir una función que almacene las asignaturas de un curso (por ejemplo, 
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota 
que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En 
<asignatura> has sacado <nota> donde <asignatura> es cada una de las asignaturas de 
la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""

def ing_int(arg):
    return int(input(arg))

def compNotas(arg):
    notas = ing_int(arg)
    return notas if(1 <= notas <= 10) else compNotas("Datos erroneos, ingrese nuevamente: ")

def pedirNotas(mat):
    notas = []
    for i in range(len(mat)):
        notas.append(compNotas("Ingrese su nota de la materia " + mat[i] + ": "))
    return notas

def salida(notas,mat):
    for i in range(len(notas)):
        print("En la asignatura",mat[i],"ha sacado:",notas[i])

def p_matNotas():
    mat = ["Matemáticas","Física","Química","Historia","Lengua"]
    notas = pedirNotas(mat)
    salida(notas,mat)

p_matNotas()