"""
Ejercicio 10:
Escribir una función que pregunte el nombre de un producto, su precio y 
un número de unidades y muestre por pantalla una cadena con el nombre del producto 
seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades 
con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

def ingr_str(arg):
    return str(input(arg))

def salida_ej10(nomb,prec:float,cant:int):
    total = prec * cant
    print("%s: %003d con cada unidad a precio de $%0000006.2f; El total es %000000008.2f" % (nomb,cant,prec,total))
    
def p_Ej10():
    nomb,prec,numb = input("Ingrese el nombre de un producto, su precio"
                        + " y la cantidad de productos, cada uno separado por una coma:\n").split(",")
    prec = float(prec)
    numb = int(numb)
    salida_ej10(nomb,prec,numb)
  
p_Ej10()