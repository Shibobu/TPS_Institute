"""
Ejercicio 14: Lea los valores de los lados de un triángulo. Determine y muestre un 
mensaje correspondiente a su tipo (1. EQUILÁTERO, 2. ISÓSCELES, O 3. ESCALENO)
"""

def ing_float(arg):
    return float(input(arg))

def comp_pos(num):
    return False if(num < 0) else True

def cont_lado(arg):
    lado = ing_float(arg)

    while not comp_pos(lado):
        lado = ing_float("Datos erroneos, ingrese nuevamente: ")
    
    return lado


def p_triangulos():
    lad1 = cont_lado("Ingrese el primer lado: ")
    lad2 = cont_lado("Ingrese el segundo lado: ")
    lad3 = cont_lado("Ingrese el tercer lado: ")
   
    if(lad1 != lad2 != lad3):
        print("EL triangulo es escaleno")
    elif (lad1 == lad2 == lad3):
        print("El triangulo es equilatero")
    else: print("El triangulo es iscoseles")

p_triangulos()