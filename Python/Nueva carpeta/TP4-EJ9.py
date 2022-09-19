"""
Ejercicio 9:
Un profesor desea saber el porcentaje de varones y mujeres de
su clase sabiendo que tiene N alumnos en total, CV varones,
CM mujeres
"""

def ingr(arg):
    return int(input(arg))

def porc(ohPerc,perc): #50
    
    perc *= 100

    if perc == 0:
        return 0
    else:   # 0.5
    # ohPerc -----> 100%
    # perc -------> x
        return perc // ohPerc

def porcAl():
    b = True

    while b : 

        total = ingr("Ingrese el total de alumnos en el aula: ")
        CV = ingr("Ingrese la cantidad de varones en el aula: ")
        CM = ingr("Ingrese la cantidad de mujeres en el aula: ")

        if (CV + CM) != total:
            salida("Algo esta mal, ingrese nuevamente por favor")
        else: b= False

    salida("Porcentaje de varones en el aula: " 
            + str(porc(total,CV))
            + "%")

    salida("Porcentaje de mujeres en el aula: " 
            + str(porc(total,CM))
            + "%")

def salida(arg):
    print(arg)

if __name__ == "__main__":
    porcAl()