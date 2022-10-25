
def suma (a,b):
    try:
        return float(a + b)
    except:
        print("Error de Tipos de datos, no se puede restar un int con un String")

def resta(a,sustraendo):
    return suma(a, -sustraendo)


def division(a, divid):
    try:
        return float(a / divid)
    except:
        if divid == 0:
            print("Error, Division por cero")
        else:
            print("No se puede dividir entre un int y un string")

def multip(fac1,fac2):
    try:
        return float(fac1*fac2)
    except:
        print("No se puede dividir entre un numero y un string")