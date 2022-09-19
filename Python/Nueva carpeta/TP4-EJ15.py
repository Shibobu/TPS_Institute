"""
Ejercicio 15:
El costo de un automóvil nuevo para un comprador es la suma total del 
costo del vehículo, del porcentaje de la ganancia del vendedor y de los impuestos locales 
o estatales aplicables (sobre el precio de venta). Suponer una ganancia del vendedor del 
12% en todas las unidades y un impuesto del 6% y diseñar un algoritmo para leer el costo
total del automóvil e imprimir el costo para el consumidor.
"""


def ingr(arg):
    return int(input(arg))

def descPerc(cost, perc):
        perc /= 100
        return cost * perc

def costoAutomovil():
    costo = ingr("Ingrese el costo del vehiculo $")
    total = costo

    # Gcia del Vendedor
    total += descPerc(costo, 12)

    # Impuestos locales y o estatales
    total += descPerc(costo, 6)
    cad = ("El total del vehiculo es: $" 
        + str(total))

    salida(cad)
    

def salida(arg):
    print(arg)

if __name__ == "__main__":
    costoAutomovil()
