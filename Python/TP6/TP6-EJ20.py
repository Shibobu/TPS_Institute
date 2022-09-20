"""
Ejercicio 20: Los tramos impositivos mensuales para la declaración de la renta en un 
determinado país son los siguientes:
Renta Tipo impositivo
Menos de $10000 5%
Entre $10000 y $20000 15%
Entre $20000 y $35000 20%
Entre $35000 y $60000 30%
Más de $60000 45%
Escribir un programa que pregunte al usuario su renta mensual y muestre por pantalla 
el tipo impositivo que le corresponde y el valor a abonar.
"""
def ing_float(arg):
    return float(input(arg))

def ingreso(arg):
    cons = ing_float(arg) 
    return cons if(cons > 0) else ingreso("Datos erroneos, ingrese nuevamente: ")

def renta():
    rent = ingreso("Ingrese su renta mensual: ")

    match rent:
        case rent if(rent < 10000):
            print("Le corresponde el tipo impositivo, Menor a 10000 de un 5% y debe abonar: $",rent*0.05)
        case rent if(10000 <= rent < 20000 ):
            print("Le corresponde el tipo impositivo, Entre 10000 y 20000 de un 15% y debe abonar: $",rent*0.15)
        case rent if(20000 <= rent < 35000 ):
            print("Le corresponde el tipo impositivo, Entre 20000 y 35000 de un 20% y debe abonar: $",rent*0.20)
        case rent if(35000 <= rent < 60000 ):
            print("Le corresponde el tipo impositivo, Entre 35000 y 60000 de un 30% y debe abonar: $",rent*0.30)
        case default: print("Le corresponde el tipo impositivo, Mayor a 60000 de un 45% y debe abonar: $",rent*0.45)

renta()