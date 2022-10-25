"""
Menu para el TP9
"""

from Mylibrary import *

# Trabajo Practico Nº 9 Ejercicio 1
def contra(passw):
    arg = "Ingrese la contraseña: "
    while ing_str(arg) != passw:
        arg = "Equivocado, Ingrese la contraseña nuevamente: "
    print("Bienvenido !")

def p_TP1():
    passw = ing_str("Ingrese la constraseña para establecer la cuenta: ")
    contra(passw)

#Trabajo Practico Nº 9 Ejercicio 2
def set_obj():
    return ing_floatpox("Ingrese el monto objetivo de ahorro $")

#Registra los depositos
def depositos(obj):
    while obj > 0 :
        obj -= ing_floatpox("Deposita: $")
        print("Saldo ${sal}".format(sal=obj))
    return obj

def p_TP2():
    obj = set_obj()
    aux = depositos(obj)
    print("Se llego al monto objetivo ${ob}".format(ob = obj))
    if aux < 0: 

        aux = abs(aux)
        print("Quedo un resto de ${res}".format(res=aux))

#Trabajo Practico Nº 9 Ejercicio 3

def menutp3():
    print("Seleccione una opcion: \n"
        + "1---------Comenzar el programa \n"
        + "2---------Imprimir listado \n"
        + "3---------Finalizar el programa \n")
    op = ing_int("Ingrese una opcion: ") 
    return op if op != 0 else menutp3()

def seleccion(op):

    match(op):
        case 1: 
            print("Acchi Kocchi")
        case 2:
            print("Doki Doki Waku Waku")
        case 3:
            print("Salir")
            return 0
        case _:
            print("Opcion no existente, porfavor ingrese nuevamente")
    return -1

def p_TP3():

    while seleccion(menutp3()) !=  0:
        continue

# Trabajo Practico Nº 9 Ejercicio 4
def dig(num):
    d = num % 10
    num /= 10
    return trunc(num),d

def dig_par_impar(num):
    aux = num
    p = 0
    i = 0
    while aux > 0:
        aux,d = dig(aux)
        if d % 2 == 0:
            p += 1
        else : i+=1

    print("La cantidad de digitos pares del numero {n} es: {par} \n".format(n=num,par=p)
        +"La cantidad de digitos impares del numero {n} es: {impar}\n".format(n= num, impar=i))
    
    return p,i
        
def p_TP4():
    pares = 0
    impares = 0
    while True:
        num = ing_int("Ingrese un numero entero\nO ingrese 0 para salir del programa: ")

        if num == 0:
            break
        if num < 0:
            continue
        p,i = dig_par_impar(num)
        pares += p
        impares += i

    print("El total de digitos pares es: ",pares)
    print("El total de digitos inpares es: ",impares)

# Trabajo Practico Nº 9 Ejercicio 5
def multiplo(pd):
    while pd % 3 != 0:

            pd +=1
    return pd

def p_TP5():
    sum = 0
    pd = 1
    while pd < 100:
        pd = multiplo(pd)
        sum += pd
        pd += 1

    print ("La sumatoria de los multiplos de 3 entre 0 y 100 es:", sum)
    
#Trabajo Practico Nº 9 Ejercicio 6

def p_TP6():
    cantP = 0
    sumP = 0
    sumN = 0 
    i = 1

    while True:
        x = ing_zero("Ingrese el {ix}° Numero entero: ".format(ix = i))
        if x < 0:
            sumN+= x
        else:
            sumP+= x
            cantP += 1

        i += 1

        if i > 6:
            break
    try:
        print("El promedio de numeros positivos es: ", sumP/cantP)
    except:
        print("No hay numeros positivos cargados")
    
    print("La sumatoria de numeros negativos es:",sumN)

#Menu
def opciones():
    print("---------Ingrese un ejercicio del Trabajo Practico:\n" +
        "--------- 1) Ejercicio 1\n" +
        "--------- 2) Ejercicio 2\n" +
        "--------- 3) Ejercicio 3\n" +
        "--------- 4) Ejercicio 4\n" +
        "--------- 5) Ejercicio 5\n" +
        "--------- 6) Ejercicio 6\n" +
        "--------- 7) Salida\n")
    return ing_int("Ingrese una opcion: ")

def switch():
    op = opciones()
    match op:
        case 1:
            p_TP1()
        case 2:
            p_TP2()
        case 3:
            p_TP3()
        case 4:
            p_TP4()
        case 5:
            p_TP5()
        case 6:
                p_TP6()
        case 7:
            print("Salir")
            return 0
        case _:
                print("Valor incorrecto, ingrese nuevamente: ")
    return 1

if __name__ == "__main__":
    while switch():
        continue
