"""
Ejercicio 10:
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus 
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones 
por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en 
cuenta su sueldo base y comisiones.
"""
def ingr(arg):
    return int(input(arg))

def ing_ej10():
    b = True

    while b:
        sueldo = ingr("Ingrese el sueldo base ")

        if sueldo < 0:
            print("Algo esta mal")
        else: b = False
    return sueldo

def suel_emp():

    sueldo = ing_ej10()
    comm = 0 

    for i in range(0,3):
        v1 = ingr("Ingrese el total de la " + str(i+1) + "º venta ")
        comm += (v1 * 0.1)
    
    salida("El vendedor recibira: " 
            + str(comm) 
            + " en comisiones")
    salida("El vendedor recibira en el mes:"
            + str(sueldo + comm)
            + " en total")

def salida(arg):
    print(arg)

if __name__ == "__main__":
    suel_emp()