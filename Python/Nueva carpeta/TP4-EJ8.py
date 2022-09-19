"""
Ejercicio 8:
Ingresar el radio de una circunferencia y calcular:
    Perimetro de la circunferencia
    Superficie del circulo con las siguientes formulas
        PI, constante: PI = 3,141592
        Perimetro: P = 2*PI*R
        Superficie: S = PI*R^2
"""
from math import pi

def ingr(arg):
    return int(input(arg))

def persup():

    radio = ingr("Ingrese el radio de la circunferencia: ")

    per = 2* pi * radio
    sup = pi * pow(radio,2)

    salida("El perimetro de la circunferencia es: " 
            + str(per))
    salida("El area de la circunferencia es: "
            + str(sup))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    persup()
