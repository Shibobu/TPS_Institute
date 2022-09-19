"""
Ejercicio 15: Una medida de la obesidad se determina mediante el índice de masa 
corporal (IMC), que se calcula dividiendo los kilogramos de peso por el cuadrado de la 
estatura en centímetros (IMC = peso [kg]/ estatura2 [cms]). Dado el peso y la estatura 
de una persona determine el grado de obesidad según el IMC.
Tipo de Obesidad Índice de masa corporal (IMC)
Tipo 1 – Infrapeso Menos de 17
Tipo 2 – Bajo Peso Más de 17 hasta 18
Tipo 3 – Peso Normal Más de 18 hasta 25
Tipo 4 -Obesidad Tipo I Más de 25 hasta 30
Tipo 5 – Obesidad Tipo II Más de 30 hasta 35
Tipo 6 – Obesidad Tipo III Más de 35 hasta 40
Tipo 7 – Obesidad Mórbida Más de 40
"""

def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def mat_IMC(imc):
    match imc:
        case imc if imc <= 17:
            print("Infrapeso")
        case imc if(17<imc<=18):
            print("Bajo peso")
        case imc if(18<imc<=25):
            print("Peso normal")
        case imc if (25<imc<=30):
            print("Obesidad de Tipo 1")
        case imc if (30<imc<=35):
            print("Obesidad de Tipo 2")
        case imc if (35<imc<=40):
            print("Obesidad de Tipo 3")
        case default: 
            print("Obesidad Morbida")

def p_IMC():
    peso = ingreso("Ingrese el peso de la persona: ")
    estatura = ingreso("Ingrese la estatura de la persona: ")
    IMC= peso/ pow(estatura,2)
    mat_IMC(IMC)

p_IMC()
