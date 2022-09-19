"""
Ejercicio 14: Lea los valores de los lados de un triángulo. Determine y muestre un 
mensaje correspondiente a su tipo (1. EQUILÁTERO, 2. ISÓSCELES, O 3. ESCALENO)
"""

def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def p_triangulos():
    lad1 = ingreso("Ingrese el primer lado: ")
    lad2 = ingreso("Ingrese el segundo lado: ")
    lad3 = ingreso("Ingrese el tercer lado: ")
   
    if(lad1 != lad2 != lad3):
        print("EL triangulo es escaleno")
    elif (lad1 == lad2 == lad3):
        print("El triangulo es equilatero")
    else: print("El triangulo es iscoseles")

p_triangulos()