"""
Ejercicio 12:
Un alumno desea saber cuál será su calificación final en la materia de 
Programación. Dicha calificación se compone de los siguientes porcentajes:

 55% del promedio de sus tres calificaciones parciales.
 30% de la calificación del examen final.
 15% de la calificación de un trabajo final
"""
def ingr(arg):
    return int(input(arg))

def prom(sum,cant):
    return sum / cant

def not_contr(nota):
    b = True
    if nota < 1 or nota > 10:
            print("Notas incorrectas, ingrese nuevamente ")
            b = False
    return b

def ing_contr(arg):
    b= True
    
    while b: 
        par = ingr(arg)

        if  not_contr(par) : b = False
    
    return par

def sum_notas():
    par_prom = 0

    for i in range(0,3):
        par_prom += ing_contr("Ingrese la nota del " + str(i+1) + "º parcial ")
    
    return par_prom

def parciales():
    promed = prom(sum_notas(),3)
    salida("El promedio de notas es: "+ str(promed))

    final = ingr("Ingrese el resultado del examen final ")
    tp_final = ingr("Ingrese el resultado del Trabajo Practico Final ")

    nota_final = (promed*0.55) + (final*0.33) + (tp_final*0.15)

    salida("La calificacion final es: " + str(int(nota_final)))
    
def salida(arg):
    print(arg)

if __name__ == "__main__":
    parciales()