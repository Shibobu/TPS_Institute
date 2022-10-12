"""
Escribir una función que almacene las asignaturas de un curso (por ejemplo,
Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla
el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas
de la lista
"""
def showlasig(asignaturas):
    for i in asignaturas:
        print("Yo Estudio {asig}".format(asig=i))

def p_asig():
    asignaturas = ("Matematicas","Fisica","Quimica","Historia","Lengua")
    try: 
        asignaturas[1] = "Biologia"
    except:
        print("Es una tupla no se puede entrar mas valores! ")
    showlasig(asignaturas)

p_asig()