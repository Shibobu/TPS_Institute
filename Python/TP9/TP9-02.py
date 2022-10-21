"""
Ejercicio 2: Escriba una función que simule una caja de ahorros. Solicitará primero una
cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación,
solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total
ahorrado iguale y no supere al objetivo.
"""
# Controla el ingreso sea dinero y el objetivo y los depositos no sea negativos


#Setea el objetivo
from Python.TP9.Mylibrary import ing_float

def ing_floatpox(arg):
    x = ing_float(arg)
    if x < 0:
        ing_floatpox("Solo datos positivos, ingrese nuevamente: ")
def set_obj():
    ing_float("Ingrese el monto objetivo de ahorro $")

#Registra los depositos
def depositos():
    return ing_float("Deposita $")

def caja_Ahorro():
    obj = set_obj()
    aux = obj
    while aux > 0 :
        aux -= depositos()
        print("Saldo ${sal}".format(sal=aux))
        
    print("Se llego al monto objetivo ${ob}".format(ob = obj))
    if aux < 0: 
        aux = abs(aux)
        print("Quedo un resto de ${res}".format(res=aux))

caja_Ahorro()
    