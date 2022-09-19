"""
Ejercicio 14: 
El siguiente es el menú de un restaurante de bocadillos. Diseñar un 
algoritmo capaz de leer el número de unidades consumidas de cada alimento ordenado 
y calcular la cuenta total. 
Bocadillo de jamón ($ 250) 
Bocadillo de queso ($ 200) 
Papas fritas ($ 300) 
Gaseosa ($ 375) 
Cerveza ($ 450)
"""

import random

def ingr(arg):
    return int(input(arg))

def prod(num1,num2): 
    return num1*num2

def menu_Bar():
     match trueMenu_Bar():
        case 1:
            # Bocadillo de Jamon
            cant = ingr("¿Cuantos Bocadillos de jamon desea ordenar? ")
            return prod(250,cant)
        
        case 2:
            # Bocadillo de Queso
            cant = ingr("¿Cuantos Bocadillos de queso desea ordenar? ")
            return prod(200,cant)
        
        case 3:
            # Papas fritas
            cant = ingr("¿Cuantas papas fritas desea ordenar? ")
            return prod(300,cant)
        
        case 4:
            # Gaseosa
            cant = ingr("¿Cuantas gaseosas desea ordenar? ")
            return prod(375,cant)
        
        case 5:
            # Cerveza
            cant = ingr("¿Cuantas cervezas desea ordenar? ")
            return prod(450,cant)
        
        case default:
            # Salida
            return False

def restoBar():
    salida("¡Bienvenidos a Truquito Resto Bar!")
    sum = 0
    aux = menu_Bar()

    while aux:
        sum += aux
        aux = menu_Bar()
    
    cad = ("El total a pagar es: $" 
            + str(sum) 
            + "\n"
            + goodbyeMSG())
    salida(cad)

def trueMenu_Bar():
    cad = (" Elija un elemento del menu " 
            + "\n 1) Bocadillo de Jamon -----------$250"
            + "\n 2) Bocadillo de Queso -----------$200"
            + "\n 3) Papas Fritas -----------------$300"
            + "\n 4) Gaseosa ----------------------$375"
            + "\n 5) Cerveza ----------------------$450"
            + "\n Cualquier otro numero para dejar de ordenar "
            + "\n Producto: ")
    op = ingr(cad)
    return op

# Mensaje de salida!
def goodbyeMSG():
    rand = random.randrange(70)
    
    if rand <= 5:
        return "Are you enjoying the time of eve?"

    if rand >5 and rand <= 40:
        return "¡Gracias por venir!"
    
    if rand >40 and rand <= 66:
        return "¡Disfrute su comida!"

    if rand >66:
        return " "

def salida(arg):
    print(arg)

if __name__ == "__main__":
    restoBar()
