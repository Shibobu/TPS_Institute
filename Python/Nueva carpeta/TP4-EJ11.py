"""
Ejercicio 11:
Una tienda ofrece un descuento del 15% sobre el total de la compra y un 
cliente desea saber cuánto deberá pagar finalmente por su compra.
"""
def ingr(arg):
    return int(input(arg))

def desc():
    total_com = ingr("Ingrese el total de la compra: ")
    salida("El total de la compra con el 15% es: " 
            + str(total_com*0.85))

def salida(arg):
    print(arg)

if __name__ == "__main__":
    desc()