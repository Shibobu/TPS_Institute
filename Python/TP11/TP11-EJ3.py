"""
Escribir una función que pregunte una fecha en formato dd/mm/aaaa y muestre por 
pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre 
del mes en letras, recuperando el nombre del mes desde un diccionario.
"""
from Mylibrary import *

def biciesto(anio):
    if anio % 4 == 0:
        if anio % 100 & anio % 400== 0:
            return True
        return True
    else: return False

def compFech(dd,mm,aaaa):
    b = biciesto(aaaa)
    if 1 < mm < 12:
        match mm:
            case 1 , 3, 5 ,7 , 8, 10, 12:
                if 1 < dd < 31:
                    return True
            case 4, 6, 9, 11:
                if 1 < dd < 30:
                    return True
            case 2:
                if b & (1 < dd < 29):
                    return True
                elif 1 < dd < 28:
                    return True
    return False
        
def fecha():
    try:
        dd,mm,aaaa = int(ing_str("Ingrese una fecha en el formato dd/mm/aaaa").split("/"))
        if compFech(dd,mm,aaaa):
            
    except: 
        print("Debe ingresar si o si en el formato dd/mm/aaaa")
        

fecha()