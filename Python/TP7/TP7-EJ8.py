"""
Ejercicio 8: Escribir una función que pregunte por una muestra de números, separados 
por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

Media = Promedio
    Mu = Suma(ListaNum)/ len(ListaNum)

Desviacion Tipica
    Sig = sqrt(Suma(pow(ListaNum - Mu),2) / len(ListaNum))

"""


from math import sqrt


def ingstr(arg):
    return str(input(arg))

def convFloat(l1):
    for i in range(len(l1)):
        l1[i] = float(l1[i])

def med(sum,cant):
    return sum /cant

def sumaT(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum

def calcVaria(lst,mu):
    sum = 0
    for i in lst:
        sum += (pow(i-mu,2))
    return sum / (len(lst)-1)

def salida(mu, sig):
    print("La media de la muestra es {m} con una desviacion de: {s}".format(m = mu,s= sig))

def p_muestra():
    listnum = []
    listnum = ingstr("Ingrese numeros en la lista, separados por una ',': \n \t").split(",")
    convFloat(listnum)
    sum = sumaT(listnum)
    mu = med(sum,len(listnum))
    sig = calcVaria(listnum,mu)
    salida(mu,sqrt(sig))

p_muestra()