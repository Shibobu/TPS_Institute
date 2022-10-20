"""
Ejercicio 2: Escriba una función que simule una caja de ahorros. Solicitará primero una
cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación,
solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total
ahorrado iguale y no supere al objetivo.
"""
# Controla el ingreso sea dinero y el objetivo y los depositos no sea negativos
def ing_input(arg):
    try: 
        x = float(input(arg))
        if x < 0:
            ing_input("Monto erroneo, ingrese un monto correcto: ")
        return x
    except:
        ing_input("Error de Datos, ingrese un monto correcto: ")

#Setea el objetivo
def set_obj():
    return ing_input("Ingrese el monto objetivo de ahorro $")

#Registra los depositos
def depositos():
    return ing_input("Deposita $")

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
    