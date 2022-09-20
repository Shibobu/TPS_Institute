"""
Ejercicio 19: En una determinada empresa, sus empleados son evaluados al final de cada 
año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir 
aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir 
los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las 
cifras mencionadas. A continuación, se muestra una tabla con los niveles 
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es 
de $120000 multiplicada por la puntuación del nivel.
Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de 
rendimiento, así como la cantidad de dinero que recibirá el usuario.
"""


def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    punt = ing_float(arg)
    return punt if((punt <= 0.6)or(punt == 0.0)or(punt == 0.4))else ingreso("Dato Erroneo, Ingrese nuevamente: ")

def match_punt(p):
    match p:
        case 0.0:
            return "INACEPTABLE"
        case 0.4: 
            return "Aceptable"
        case p if p >= 0.6:
            return "Meritorio"

def p_Puntaje():
    punt = ingreso("Ingrese la puntuaciond el empleado: ")
    print("Su puntuacion es:",punt,match_punt(punt),"la cantidad que recibira es de: $",120000*punt)

p_Puntaje()