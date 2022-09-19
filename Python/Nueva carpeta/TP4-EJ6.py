"""
Ejercicio 6:
Calcular y mostrar el promedio de dos numeros A y B
"""

def ingr(arg):
    return int(input(arg))

def prom(sum,cant):
    return sum / cant

def promedio():
    A = ingr("Ingrese el primer numero: ")
    B = ingr("Ingrese el segundo numero: ")
    promed = prom(A+B,2)
    salida("El resultado es: " + str(promed))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    promedio()
