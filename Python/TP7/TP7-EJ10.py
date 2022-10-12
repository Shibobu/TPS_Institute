"""
Ejercicio 10: Escribir una función sum() y una función multip() que sumen y multipliquen 
respectivamente todos los números de una lista aleatoria. Por ejemplo: sum([1,2,3,4]) 
debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""
from random import  random, seed


def sum(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def multip(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul

def fill(lst):
    seed()
    lst.append(random()*(-10 - 10)+ 10)
    op = int(input("¿Desea seguir cargando?\n \t 1 - Si 0 -No \n Ingreso: "))
    if op != 0: 
        fill(lst)
        return 1
    else: return 0

def p_sumMul():
    lst = []
    fill(lst)
    print("La lista es:",lst,"\n Su suma es:",sum(lst),"\n Su multiplicacion es:",multip(lst))

p_sumMul()