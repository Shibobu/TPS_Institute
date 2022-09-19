"""
Ejercicio 6: En un almacén se descuenta 20% del precio al cliente si el valor a pagarse es 
mayor a $200. Dado un valor de precio, muestre lo que debe pagar el cliente.
"""

def ing_float(arg):
    return float(input(arg))

def salida(pago):
    print("El cliente debe pagar:",pago)

def p_desc():
    pago = ing_float("Ingrese el precio: ")
    
    if pago > 200:
        salida(pago*0.8)
    else: salida(pago)

p_desc()