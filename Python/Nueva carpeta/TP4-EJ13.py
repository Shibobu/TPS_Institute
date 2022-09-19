"""
Ejercicio 13:
Queremos conocer los datos estadísticos de una asignatura, por lo tanto, 
necesitamos un programa que lea el número de suspensos, aprobados, notables y 
sobresalientes de una asignatura, y nos devuelva: 

a.- El tanto por ciento de alumnos que han superado la asignatura. 
b.- El tanto por ciento de suspensos, aprobados, notables y sobresalientes de 
la asignatura.

"""

def ingr(arg):
    return int(input(arg))

def porc(ohPerc,perc): #50
    
    if perc == 0:
        return 0
    else:   # 0.5
    # ohPerc -----> 100%
    # perc -------> x
        return perc * 100 // ohPerc


def proc_Alumn():

    sus = ingr("Ingrese el numero de alumnos supendidos: ")

    b = True

    while b:
        aprob= ingr("Ingrese la cantidad de alumnos aprobados: ")
        notab = ingr("Ingrese la cantidad de alumnos notables: ")
        sobre = ingr("Ingrese la cantidad de alumnos sobresalientes: ")

        if(notab + sobre <= aprob): b = False
        else : print("Error, los alumnos aprobados no deben ser" 
                    + " menor que la suma de los notables y sobresalientes"
                    + "\nIngrese los valores nuevamente")
    
    total= sus + aprob
    print(total)

    print(sus)
   
    sus = porc(total,sus)
    aprob = porc(total,aprob)
    notab = porc(total,notab)
    sobre = porc(total,sobre)

    salid_Alum(sus,aprob,notab,sobre)


def salid_Alum(sus, aprob,notab,sobre):
    cad = ("El porcentaje de alumnos que superaron la materia es: " 
            + str(aprob) + "%" 
            + "\nResultado de todos los alumnos: "
            + "\nEl porcentaje de alumnos que fallaron la materia es: "
            + str(sus) + "%" 
            + "\nEl porcentaje de alumnos que superaron la materia es: " 
            + str(aprob) + "%" 
            + "\nEl porcentaje de alumnos notables en la materia: "
            + str(notab) + "%" 
            + "\nEl porcentaje de alumnos sobresalientes en la materia: "
            + str(sobre)) + "%"

    salida(cad)

def salida(arg):
    print(arg)

if __name__ == "__main__":
    proc_Alumn()