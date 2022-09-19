"""
Ejercicio 8:
Escribir una función que pregunte al usuario la fecha de su nacimiento en 
formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
"""


def ingr_str(arg):
    return str(input(arg))

def comp_Bic(year:int):
    if year % 400 == 0:
        return True
    if (year % 100 != 0) & (year % 4 == 0):
        return True
    return False

def salida(arg):
    print(arg)

def compDay(dd:int,mm:int,aaaa:int):

    if dd > 0:
        match mm:
            case mm if (((mm <=7) & (mm %2 != 0)) or ((mm >7) & (mm % 2 == 0))):
                # 31 days
                if dd <= 31:
                    return True

            case mm if(((mm < 7) & (mm %2 == 0)) or (mm >7) & (mm % 2 != 0)):
                # 30 days
               if dd <= 30:
                    return True
                
            case  2:
                if (comp_Bic(aaaa) & dd <= 29):
                    return True
                if dd <= 28:
                    return True
            case mm if ((mm < 1 ) or (mm > 12)):
                salida("MES INCORRECTO")
                return False
        salida("Dia equivocado")
        return False


def p_Ej8():
    dd,mm,aaaa = ingr_str("Ingrese su fecha de nacimiento de la siguiente forma: "
                    + "dd/mm/aaaa: ").split('/')
    
    if compDay(int(dd), int(mm), int(aaaa)):
        cad = ( "Dia: " + dd 
                +"\nMes: "+ mm
                +"\nAño: "+ aaaa)
        salida(cad)

p_Ej8()
    