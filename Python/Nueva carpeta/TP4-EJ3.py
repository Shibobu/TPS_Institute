"""
Ejercicio 3:
Calcular la suma de dos valores ingresados por el usuario
"""
def ingr(arg):
    return int(input(arg))

def suma():
    num1 = ingr("Ingrese el primer numero a sumar: ")
    num2 = ingr("Ingrese el segundo numero a sumar: ")
    salida("El resultado es: " + str(num1+num2))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    suma()
