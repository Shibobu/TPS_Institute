"""
 Escribir una función que permita al usuario ingresar 6 números enteros, que 
pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números 
negativos y el promedio de los positivos. Cabe recordar que no es posible dividir por 
cero, por lo que es necesario controlar que la función no permita su ingreso.
"""

from Mylibrary import ing_int


def ing_ent(arg):
    x = ing_int(arg)
    return x if x != 0 else ing_ent("No se permiten numeros iguales a cero, Ingrese nuevamente: ")

def sum():
    cantP = 0
    sumP = 0
    sumN = 0 
    i = 1

    while True:
        x = ing_ent("Ingrese el {ix}° Numero entero: ".format(ix = i))
        if x < 0:
            sumN+= x
        else:
            sumP+= x
            cantP += 1

        i += 1

        if i > 6:
            break
    try:
        print("El promedio de numeros positivos es: ", sumP/cantP)
    except:
        print("No hay numeros positivos cargados")
    
    print("La sumatoria de numeros negativos es:",sumN)

if __name__ == "__main__":
    sum()
    