"""
Escribir un programa que solicite la cantidad de
kilometros recorridos por un auto y la cantidad
total de litros que consumio en ese recorrido.
Luego mostrar por pantalla el consumo de
combustible por kilometro
"""

print("Ingrese la cantidad de kilometros recorridos")
km = int(input())
print("Ingrese la cantidad de litros consumidos")
lt = int(input())
print("La cantidad de litros consumidos por "
        + "kilometros, es: " + str(lt/km))
