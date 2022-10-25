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

from operaciones import *


if __name__ == "__main__":
    a = 10
    b = 5
    c = 0
    d = "Hola"
    
    print (suma(a,b))
    print (resta(a,b))
    print(division(a,b))
    print (multip(a,d))