"""
Ejercicio 16: En determinada ciudad la tarifa eléctrica varía de acuerdo a la estación del 
año y el consumo en la residencia, según la siguiente tabla:
Consumo en KW/h Invierno($) Verano($) Otoño-Primavera($)
< 130              0.04       0.04          0.00
130 a 500          0.08       0.11          0.03
500 a 700          0.11       0.13          0.02
> 700              0.16       0.26          0.10
Conociendo el consumo en una residencia y la estación del año que no encontramos 
indicar cuál es el importe a pagar por el consumo eléctrico en dicha residencia
"""

def ing_float(arg):
    return float(input(arg))

def ing_int(arg):
    return int(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def ingreso_int(arg):
    num = ing_int(arg)
    return num if(num>0 & num <= 3) else ingreso_int("Datos erroneos, Ingrese nuevamente: ")

def prod(num1,num2):
    return num1*num2

def comp_cons(cons):
    match cons:
                case cons if(cons <= 130): return 0
                case cons if(130 < cons < 500): return 1
                case cons if(500 < cons < 700): return 2
                case default: return 3

def match_estacion(cons):
    op = ingreso_int("---Elija la estacion del año actual---"
                    +"\n1----------Invierno"
                    +"\n2----------Verano"
                    +"\n3----------Primavera u Otoño"
                    +"\nOpcion: ")
                    
    invierno = [0.04,0.08,0.11,0.16]
    verano = [0.04,0.11,0.13,0.26]
    privoto= [0,0.03,0.02,0.10]

    match op:
        case 1:
            cons = prod(cons,invierno[comp_cons(cons)])
        case 2:
            cons = prod(cons,verano[comp_cons(cons)])
        case default:
            cons = prod(cons,privoto[comp_cons(cons)])
            
        
    salida(cons)

def salida(cons):
    print("El consumo de la casa es:",cons)

def p_consumoHogar():
    cons = ingreso("Ingrese el consumo de una casa: ")
    match_estacion(cons)

p_consumoHogar()