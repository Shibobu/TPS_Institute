"""
Ejercicio 1: Escribir una función que almacene las asignaturas de un curso (por ejemplo,
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
def show(mat):
    for i in mat:
        print(i)

def p_asignaturas():
        
    mat = ["Matemáticas","Física","Química","Historia","Lengua"]
    show(mat)

p_asignaturas()