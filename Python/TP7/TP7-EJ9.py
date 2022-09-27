"""
Ejercicio 9: Escribir una función que calcule la longitud de una lista o una cadena dada. 
(no utilizar la función de python len() incorporada).
"""

def long(lst):
    n = 0
    
    for i in lst:
        n+=1
    
    return n

def p_long(): 
    lst = [1,2,6,94,1,44,61,-1641]
    print("Size: ",long(lst))
    lst = "Programming is iz"
    print("Size: ",long(lst))

p_long()