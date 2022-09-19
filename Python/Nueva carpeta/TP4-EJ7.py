"""
Ejercicio 7:
Calcular el area de un triangulo dada su base y altura
Formula para aplicar: sup =(base*altura)/2
"""

def ingr(arg):
    return int(input(arg))

def trigsup():
    base = ingr("Ingrese la base del triangulo: ")
    height = ingr("Ingrese la altura del triangulo: ")
    sup = base*height*pow(2,-1)
    salida("El area del triangulo es: " + str(sup))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    trigsup()
