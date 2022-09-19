"""
Ejercicio 11: Ingresadas las notas de dos parciales de un estudiante, indicar el estado del 
alumno según su nota final (de 0 a 3.99 → Libre, de 4 a 6.99 → Regular y de 7 a 10 → 
Promocionado). La nota final es el promedio de ambos parciales.
"""

def ing_float(arg):
    return float(input(arg))

def suma(num1,num2):
    return num1+num2

def prom(sumado,cant):
    return sumado/cant
  
def comprNota(parcial):
    return False if ((parcial < 0) or (parcial > 10 )) else True

def ingr_nota(arg):

    parcial = ing_float(arg)
    
    while not comprNota(parcial):
        print("Nota incorrecta, por favor ingrese nuevamente: ")
        parcial = ing_float("Ingrese la nota del primer parcial: ")
    
    return parcial

def def_estado(prom): 
    match prom:
        case prom if(0 >= prom < 4):
            print("El estado del alumno es Libre")
        case prom if(4 >= prom < 7):
            print("El estado del alumno es Regular")
        case prom if(7 >= prom < 10):
            print("El estado del alumno es Promocionado")

def p_NotaFinal():

   parcial1 = ingr_nota("Ingrese la nota del primer parcial: ")
   parcial2 = ingr_nota("Ingrese la nota del segundo parcial: ")
   promedio = prom(suma(parcial1,parcial2),2)
   def_estado(promedio)

p_NotaFinal()