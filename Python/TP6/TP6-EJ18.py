"""
Ejercicio 18: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al 
sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la 
M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un 
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo 
que le corresponde.
"""
def ing_cad(arg):
    return str(input(arg))

def ingresoChar(arg):
    sexs:str= "mf"
    char= ing_cad(arg)
    return char.lower() if ((char.__len__() == 1) &(sexs.__contains__(char.lower()))) else ingresoChar("Datos Erroneos, Ingrese nuevamente: ")

def p_Grupos():
    name = ing_cad("Ingrese su nombre: ")
    sex = ingresoChar("Ingrese su sexo: "
                        + "\nM/m----- Masculino"
                        + "\nF/f----- Femenino"
                        + "\n Opcion: ")
    if sex == "m":
        if name[0].upper > "N":
            print("Perteneces al Grupo A")
        else: print("Perteneces al Grupo B")
    elif name[0].upper < "M":
        print("Perteneces al Grupo A")
    else: print("Perteneces al Grupo B")

p_Grupos()