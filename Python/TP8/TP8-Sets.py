"""
Ejercicio 2: Escribir una función que almacene las asignaturas de un curso (por ejemplo, 
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla 
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas 
de la lista.
"""

def p_rep():
  materias = {"Matematicas","Fisica","Quimica","Historia","Lengua"}
  materias.add("Matematicas")
  materias.add("Biologia")
  for i in materias:
    print("Yo estudio {mat}".format(mat= i))
p_rep()