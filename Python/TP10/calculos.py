"""
Ejercicio 1:
Crea el módulo denominado operaciones.py que contendrá 4 funciones para realizar una 
suma, una resta, una multiplicación y una división entres dos números. Todas ellas 
devolverán el resultado.

En las funciones del módulo deberá de haber tratamiento e invocación manual de 
errores para evitar que se quede bloqueada una funcionalidad, eso incluye:

 Error_de_Tipos: En caso de que se envíen valores a las funciones que no sean 
números. Además, deberá aparecer un mensaje que informe Error: Tipo de dato 
no válido.

 Error_Division_Zero: En caso de realizar una división por cero. Además, deberá 
aparecer un mensaje que informe Error: No es posible dividir entre cero.

Una vez creado el módulo, crear un script calculos.py en el mismo directorio en el que 
se deberá importar el módulo y realizar la solicitud de 2 números al usuario y la 
correspondiente selección de la operación a realizar a través de un menú.

Ejemplo de prueba:
a=10 
b=5
c=0

d=”Hola”  suma(a+b) tiene que resultar 15
 resta(b-d) tiene que resultar Error_Division_Zero
 multiplicacion(b*b) tiene que resultar 25
 division(a/c) tiene que resultar Error_de_Tipos
"""

from Mylibrary import *
from operaciones import *

def menu():
    print("-----------Ingrese una opcion:\n " +
        "1) ------ Sumar\n" + " 2) ------ Resta\n" +
        "3) ------ Multiplicar\n" + "4) ------ Dividir\n"+
        "5)------- Salir")
    return ing_int("Ingrese una opcion: ")

if __name__ == "__main__":
    a = ing_float("Ingrese un valor: ")
    b = ing_float("Ingrese un segundo valor: ")
    while True:
        
        op = menu()
        match op:
            case 1:
                print(suma(a,b))
            case 2:
                print(resta(a,b))
            case 3:
                print(multip(a,b))
            case 4:
                print(division(a,b))
            case 5:
                print("Salir")
                break
        a = ing_float("Ingrese un valor: ")
        b = ing_float("Ingrese un segundo valor: ")
