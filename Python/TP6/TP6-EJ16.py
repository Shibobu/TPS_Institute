"""
Ejercicio 16: En determinada ciudad la tarifa eléctrica varía de acuerdo a la estación del 
año y el consumo en la residencia, según la siguiente tabla:
Consumo en KW/h Invierno($) Verano($) Otoño-Primavera($)
< 130              0.04       0.04          0.00
130 a 500          0.08       0.11          0.03
500 a 700          0.11       0.13          0.02
> 700              0.16       0.26          0.10
Conociendo el consumo en una residencia y la estación del año que no encontramos 
indicar cuál es el importe a pagar por el consumo eléctrico en dicha residencia
"""

def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def p_consumoHogar():
    cons = ingreso("Ingrese el consumo de una casa: ")
    