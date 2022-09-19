"""
Ejercicio 4:
Escribir un programa que solicite el ingreso de una letra,
luego valide se es una vocal mostrando el mensaje
"Es vocal" o "No es vocal"
"""

letter = str(input())
letter = letter.lower()
vowels = "aeiou"

if (letter <= "z") & (letter >= "a"):

    if(vowels.__contains__(letter)):
        print("Es vocal")
    else: print("No es vocal")


