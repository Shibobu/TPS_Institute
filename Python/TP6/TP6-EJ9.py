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

def compPos():
    kg = ing_float("Ingrese la cantidad de kilos que va a llevar: ")
    kg= False if kg < 0 else kg
    return kg

def descuento(perc):
    return 1-(perc/100)

def p_descXKilo():
    precio = ing_float("Ingrese el precio de las manzanas: ")
    kg = False
    while kg == False: 
        kg = compPos()

    match kg:
        case kg if ((kg > 2)&(kg <=5)):
            total = precio * descuento(10)
        case kg if ((kg >5) & (kg <=10)):
            total = precio * descuento(15)
        case kg if (kg > 10):
            total = precio * descuento(20)
        case default: 
            total = precio

    print("El cliente pagara: ",total*kg)

p_descXKilo()