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
            case 1 | 3| 5 |7 | 8| 10| 12:
                if 1 < dd < 31:
                    return True
            case 4 | 6| 9| 11:
                if 1 < dd < 30:
                    return True
            case 2:
                if b & (1 < dd < 29):
                    return True
                elif 1 < dd < 28:
                    return True
    return False
        
def fecha():
    meses = {1 : "Enero",2 : "Febrero",
             3 : "Marzo",4 : "Abril",
             5 : "Mayo", 6 : "Junio",
             7 : "Julio", 8 : "Agosto",
             9 : "Septiembre", 10 : "Octubre",
             11 : "Noviembre", 12 : "Diciembre"}
    try:
        dd,mm,aaaa = ing_str("Ingrese una fecha en el formato dd/mm/aaaa: ").split('/')
        dd = int(dd)
        mm = int(mm)
        aaaa = int(aaaa)
        if not compFech(dd,mm,aaaa):
            print("La Fecha ingresada es una fecha inexistente")
        else:
            print("La fecha es: {d} de {m} del año {a}".format(d = dd, m = meses.get(mm) , a = aaaa))
    except: 
        print("Debe ingresar si o si en el formato dd/mm/aaaa")
        