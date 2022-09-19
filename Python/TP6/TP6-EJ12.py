"""
Ejercicio 12: Un comercio ofrece descuentos según el monto total de compra: hasta 
$49.99 no ofrece descuento, de $50 a $149.99 ofrece 12.25% de descuento y de $150 o 
más ofrece 15% de descuento. Un cliente que compró N productos iguales a un precio 
P desea saber el monto total que debe pagar.
"""

def ing_int(arg):
    return int(input(arg))

def ing_float(arg):
    return float(input(arg))

def ingreso_int(arg):
    num = ing_int(arg)
    return num if(num>0) else ingreso_int("Datos erroneos, Ingrese nuevamente: ")

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def descuento(total,perc):
    return (total*(1-perc/100))

def salida(arg):
    print("El total de la compra es:",arg)

def match_disc(total):
    match total:
        case total if (total < 50):
            salida(total)
        case total if (50 <= total < 150):
            salida(descuento(total,12.25))
        case total if (total >= 150):
            salida(descuento(total,15))
            
def p_descuentos():
    N = ingreso_int("Ingrese la cantidad de productos que lleva el cliente: ")
    P = ingreso("Ingrese el precio de los productos: ")
    total = P*N
    match_disc(total)

p_descuentos()

   
