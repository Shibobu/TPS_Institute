"""
Ejercicio 9: Una frutería ofrece las manzanas con descuento según la siguiente tabla:
Numero de kilos comprados % Descuento
0 – 2 0%
2.01 – 5 10%
5.01 – 10 15 %
10.01 en adelante 20%
Dado el precio por kilo, y el peso, determinar cuánto pagará una persona que compre 
manzanas en esa frutería.
"""


def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(0 < cons) else ingreso("Datos erroneos, ingrese nuevamente: ")

def descuento(perc):
    return 1-(perc/100)

def p_descXKilo():
    precio = ingreso("Ingrese el precio de las manzanas: ")
    kg = ingreso("Ingrese la cantidad de kg comprados: ")

    match kg:
        case kg if ((2 < kg <=5)):
            total = precio * descuento(10)
        case kg if (5 < kg <= 10 ):
            total = precio * descuento(15)
        case kg if (kg > 10):
            total = precio * descuento(20)
        case default: 
            total = precio

    print("El cliente pagara: ",total*kg)

p_descXKilo()