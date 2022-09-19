"""
Ejercicio 4:
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extensión donde 
el prefijo es el código del país +54, y la extensión tiene tres dígitos (por 
ejemplo +54-915-5825310). Escribir una función que pregunte por un número de 
teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y 
la extensión.

"""

def ingr_str(arg):
    return str(input(arg))

def sal_telef(txt):
    print("El numero del telefono es: ",txt[4:12])

def salida(txt):
    print(txt)

def p_telef():
    num = ingr_str("Ingrese un numero de telefono de la siguiente forma: " + 
                    "Prefijo-Numero-Extension: ")
    if num.__len__()!=15:
        salida("EL NUMERO DE TELEFONO INGRESADO ES ERRONEO")
    else: sal_telef(num)

p_telef()