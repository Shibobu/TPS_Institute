"""
Ejercicio 16: Una institución educativa ha recibido una donación especial que será 
repartida entre las carreras de Telecomunicaciones, Sistemas, Administración y 
Contabilidad de la siguiente:
Telecomunicaciones: 20%
Sistemas: 15%
Administración: 30%
Contabilidad: el resto de la donación.
Diseñe un programa que determine cuánto recibirá cada carrera

"""

def ingr(arg):
    return int(input(arg))

def descPerc(cost, perc):
    perc /= 100
    return cost * perc

def repartija():
    donacion = ingr("Ingrese el total de la donacion: $")
    tele = descPerc(donacion,20)
    sist = descPerc(donacion,15)
    admin = descPerc(donacion,30)
    cont = donacion -(tele + sist + admin)
    cad = ("Repartija de la donacion entre las areas de la institucion: " 
            + "\n-------El total de la donacion es: $" + str(donacion)
            + "\n-------Telecomuniaciones le corresponde un 20% de la donacion, siendo: $" + str(tele)
            + "\n-------Sistemas le corresponde un 15% de la donacion, siendo: $" + str(sist)
            + "\n-------Administracion le corresponde un 30% de la donacion, siendo: $" + str(admin)
            + "\n-------El restante, le corresponde a Contabilidad, siendo un 35% :$" + str(cont))
    salida(cad)

def salida(arg):
    print(arg)

if __name__ == "__main__":
    repartija()