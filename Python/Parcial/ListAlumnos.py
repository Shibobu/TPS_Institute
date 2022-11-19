from Mylibrary import ing_int
from DataGenerator import genCompl

def regAlumn(alum):
    n = 5
    i = 0
    while i < n:

        alum.append(genCompl())

        i+= 1
        a = -1
        if i == n & n < 50:
            a = ing_int("Desea seguir cargando alumnos?\n"
                        + "Si es asi ingrese la cantidad de alumnos nuevos a cargar\n"
                        + "Si no ingrese un numero negativo: ")
        if a > 0: 
            n += a
            n = min(n,50)
    print(alum)
    print(i)
