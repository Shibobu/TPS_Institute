"""
Ejercicio 2: Escribir una función que almacene las asignaturas de un curso (por ejemplo, 
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla 
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas 
de la lista
"""

def sal_Est(mat):
    for i in mat:
        print("Yo estudio",i)

def p_materias():
    mat = ["Matematicas","Fisica","Quimica","Historia","Lengua"]
    sal_Est(mat)

p_materias()