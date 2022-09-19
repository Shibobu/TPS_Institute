"""
Ejercicio 4:
Calcular el producto de dos valores ingresados por el usuario.
"""

def ingr(arg):
    return int(input(arg))

def prod():
    num1 = ingr("Ingrese el primer numero a multiplicar: ")
    num2 = ingr("Ingrese el segundo numero a multiplicar: ")
    salida("El resultado es: " + str(num1*num2))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    prod()