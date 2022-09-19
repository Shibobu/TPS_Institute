"""
Ejercicio 3:
Escribir un programa que solicite un numero entero y
muestre por pantalla si el numero es par o no.
Recordar que un numero es par si al dividirlo por 2,
su resto es igual 0.
"""



print("Ingrese el numero a comprobar si es par o no")
pd = int(input())

if(pd%2 != 0):
    print("El numero no es par")
else: print("El numero es par")