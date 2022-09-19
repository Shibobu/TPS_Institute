"""
TP4-

Totalidad del trabajo separado por ejercicios
"""
#Imports
import datetime
import math
import random

# General Functions
def salida(arg):
    print(arg)

def ingr(arg):
    return int(input(arg))
# Ejercicio 1
"""
Ejercicio 1:
Escribir un programa que muestre un mensaje de bienvenida
"""

def mgs_bienb():
    salida("Hola" +
    "\nBienvenido a Programacion")


#Ejercicio 2
"""
Ejercicio 2:
Escribir un programa que permita ingresar al año de nacimiento de una 
persona y luego calcule su edad.
"""

def edad():
    b = True

    while b:
        anioNac = ingr("Ingrese su año de nacimiento: ")
        today = datetime.datetime.now().year
        
        if anioNac > today :
            salida("Si claro viajero del futuro, volve a ingresar")

        elif anioNac < 1890:
            salida("Deberia estar muerto, ¿Acaso eres inmortal?") 

        else:
             b=False
    salida("Su edad es: "+ str(today-anioNac))


#Ejercicio 3
"""
Ejercicio 3:
Calcular la suma de dos valores ingresados por el usuario
"""
def suma(num1,num2):
    return num1 + num2

def sumados():
    num1 = ingr("Ingrese el primer numero a sumar: ")
    num2 = ingr("Ingrese el segundo numero a sumar: ")
    salida("El resultado es: " + str(suma(num1,num2)))


#Ejercicio 4
"""
Ejercicio 4:
Calcular el producto de dos valores ingresados por el usuario.
"""

def producto(num1,num2):
    return num1*num2

def prod():
    num1 = ingr("Ingrese el primer numero a multiplicar: ")
    num2 = ingr("Ingrese el segundo numero a multiplicar: ")
    salida("El resultado es: " + str(producto(num1, num2)))


#Ejercicio 5
"""
Ejercicio 5:
Desarrolle un programa que permita determinar la hipotenusa de un 
triángulo rectángulo conocidas las longitudes de sus dos catetos.
"""

def calc_hip(cat1, cat2):
    return math.sqrt(pow(cat1,2)+pow(cat2,2))

def hipot():
    cat1 = ingr("Ingrese el primer cateto: ")
    cat2 = ingr("Ingrese el segundo cateto: ")
    hip = calc_hip
    salida("El resultado es: " + str(hip))

#Ejercicio 6
"""
Ejercicio 6:
Calcular y mostrar el promedio de dos numeros A y B
"""

def prom(sum,cant):
    return sum / cant

def promedio():
    A = ingr("Ingrese el primer numero: ")
    B = ingr("Ingrese el segundo numero: ")
    promed = prom(suma(A,B),2)
    salida("El resultado es: " + str(promed))

#Ejercicio 7
"""
Ejercicio 7:
Calcular el area de un triangulo dada su base y altura
Formula para aplicar: sup =(base*altura)/2
"""

def trigsup():
    base = ingr("Ingrese la base del triangulo: ")
    height = ingr("Ingrese la altura del triangulo: ")
    sup =producto(base,height)
    sup = producto(sup,pow(2,-1))
    salida("El area del triangulo es: " + str(sup))

#Ejercicio 8
"""
Ejercicio 8:
Ingresar el radio de una circunferencia y calcular:
    Perimetro de la circunferencia
    Superficie del circulo con las siguientes formulas
        PI, constante: PI = 3,141592
        Perimetro: P = 2*PI*R
        Superficie: S = PI*R^2
"""
def persup():

    radio = ingr("Ingrese el radio de la circunferencia: ")

    per = producto(2, math.pi) * radio
    sup = producto(math.pi, pow(radio,2))

    salida("El perimetro de la circunferencia es: " 
            + str(per))
    salida("El area de la circunferencia es: "
            + str(sup))

#Ejercicio 9
"""
Ejercicio 9:
Un profesor desea saber el porcentaje de varones y mujeres de
su clase sabiendo que tiene N alumnos en total, CV varones,
CM mujeres
"""

def porc(ohPerc,perc): #50
    
    perc *= 100

    if perc == 0:
        return 0
    else:   # 0.5
    # ohPerc -----> 100%
    # perc -------> x
        return perc // ohPerc

def porcAl():
    b = True

    while b : 

        total = ingr("Ingrese el total de alumnos en el aula: ")
        CV = ingr("Ingrese la cantidad de varones en el aula: ")
        CM = ingr("Ingrese la cantidad de mujeres en el aula: ")

        if (suma(CV,CM)) != total:
            salida("Algo esta mal, ingrese nuevamente por favor")
        else: b= False

    salida("Porcentaje de varones en el aula: " 
            + str(porc(total,CV))
            + "%")

    salida("Porcentaje de mujeres en el aula: " 
            + str(porc(total,CM))
            + "%")

#Ejercicio 10
"""
Ejercicio 10:
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus 
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones 
por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en 
cuenta su sueldo base y comisiones.
"""

def ing_ej10():
    b = True

    while b:
        sueldo = ingr("Ingrese el sueldo base ")

        if sueldo < 0:
            print("Algo esta mal")
        else: b = False
    return sueldo

def descPerc(total, perc):
    perc /= 100
    return total * perc

def suel_emp():

    sueldo = ing_ej10()
    comm = 0 

    for i in range(0,3):
        v1 = ingr("Ingrese el total de la " + str(i+1) + "º venta ")
        comm += (descPerc(v1,10))
    
    salida("El vendedor recibira: " 
            + str(comm) 
            + " en comisiones")

    salida("El vendedor recibira en el mes:"
            + str(suma(sueldo,comm))
            + " en total")

#Ejercicio 11
"""
Ejercicio 11:
Una tienda ofrece un descuento del 15% sobre el total de la compra y un 
cliente desea saber cuánto deberá pagar finalmente por su compra.
"""

def desc():
    total_com = ingr("Ingrese el total de la compra: ")
    salida("El total de la compra con el 15% es: " 
            + str(descPerc(total_com,100 - 15)))

#Ejercicio 12
"""
Ejercicio 12:
Un alumno desea saber cuál será su calificación final en la materia de 
Programación. Dicha calificación se compone de los siguientes porcentajes:

 55% del promedio de sus tres calificaciones parciales.
 30% de la calificación del examen final.
 15% de la calificación de un trabajo final
"""

def not_contr(nota):
    b = True
    if nota < 1 or nota > 10:
            salida("Notas incorrectas, ingrese nuevamente ")
            b = False
    return b

def ing_contr(arg):
    b= True
    
    while b: 
        par = ingr(arg)

        if  not_contr(par) : b = False
    
    return par

def sum_notas():
    par_prom = 0

    for i in range(0,3):
        par_prom += ing_contr("Ingrese la nota del " + str(i+1) + "º parcial ")
    
    return par_prom

def parciales():
    promed = prom(sum_notas(),3)
    salida("El promedio de notas es: "+ str(promed))

    final = ingr("Ingrese el resultado del examen final ")
    tp_final = ingr("Ingrese el resultado del Trabajo Practico Final ")

    nota_final = descPerc(promed,55) + descPerc(final,33) + descPerc(tp_final,15)

    salida("La calificacion final es: " + str(int(nota_final)))

#Ejercicio 13
"""
Ejercicio 13:
Queremos conocer los datos estadísticos de una asignatura, por lo tanto, 
necesitamos un programa que lea el número de suspensos, aprobados, notables y 
sobresalientes de una asignatura, y nos devuelva: 

a.- El tanto por ciento de alumnos que han superado la asignatura. 
b.- El tanto por ciento de suspensos, aprobados, notables y sobresalientes de 
la asignatura.

"""

def proc_Alumn():

    sus = ingr("Ingrese el numero de alumnos supendidos: ")

    b = True

    while b:
        aprob= ingr("Ingrese la cantidad de alumnos aprobados: ")
        notab = ingr("Ingrese la cantidad de alumnos notables: ")
        sobre = ingr("Ingrese la cantidad de alumnos sobresalientes: ")

        if(suma(notab,sobre) <= aprob): b = False
        else : print("Error, los alumnos aprobados no deben ser" 
                    + " menor que la suma de los notables y sobresalientes"
                    + "\nIngrese los valores nuevamente")
    
    total= suma(sus,aprob)
   
    sus = porc(total,sus)
    aprob = porc(total,aprob)
    notab = porc(total,notab)
    sobre = porc(total,sobre)

    salid_Alum(sus,aprob,notab,sobre)

def salid_Alum(sus, aprob,notab,sobre):
    cad = ("El porcentaje de alumnos que superaron la materia es: " 
            + str(aprob) + "%" 
            + "\nResultado de todos los alumnos: "
            + "\nEl porcentaje de alumnos que fallaron la materia es: "
            + str(sus) + "%" 
            + "\nEl porcentaje de alumnos que superaron la materia es: " 
            + str(aprob) + "%" 
            + "\nEl porcentaje de alumnos notables en la materia: "
            + str(notab) + "%" 
            + "\nEl porcentaje de alumnos sobresalientes en la materia: "
            + str(sobre)) + "%"

    salida(cad)

#Ejercicio 14
"""
Ejercicio 14: 
El siguiente es el menú de un restaurante de bocadillos. Diseñar un 
algoritmo capaz de leer el número de unidades consumidas de cada alimento ordenado 
y calcular la cuenta total. 
Bocadillo de jamón ($ 250) 
Bocadillo de queso ($ 200) 
Papas fritas ($ 300) 
Gaseosa ($ 375) 
Cerveza ($ 450)
"""

def menu_Bar():
     match trueMenu_Bar():
        case 1:
            # Bocadillo de Jamon
            cant = ingr("¿Cuantos Bocadillos de jamon desea ordenar? ")
            return prod(250,cant)
        
        case 2:
            # Bocadillo de Queso
            cant = ingr("¿Cuantos Bocadillos de queso desea ordenar? ")
            return prod(200,cant)
        
        case 3:
            # Papas fritas
            cant = ingr("¿Cuantas papas fritas desea ordenar? ")
            return prod(300,cant)
        
        case 4:
            # Gaseosa
            cant = ingr("¿Cuantas gaseosas desea ordenar? ")
            return prod(375,cant)
        
        case 5:
            # Cerveza
            cant = ingr("¿Cuantas cervezas desea ordenar? ")
            return prod(450,cant)
        
        case default:
            # Salida
            return False

def restoBar():
    salida("¡Bienvenidos a Truquito Resto Bar!")
    sum = 0
    aux = menu_Bar()

    while aux:
        sum += aux
        aux = menu_Bar()
    
    cad = ("El total a pagar es: $" 
            + str(sum) 
            + "\n"
            + goodbyeMSG())
    salida(cad)

def trueMenu_Bar():
    cad = (" Elija un elemento del menu " 
            + "\n 1) Bocadillo de Jamon -----------$250"
            + "\n 2) Bocadillo de Queso -----------$200"
            + "\n 3) Papas Fritas -----------------$300"
            + "\n 4) Gaseosa ----------------------$375"
            + "\n 5) Cerveza ----------------------$450"
            + "\n Cualquier otro numero para dejar de ordenar "
            + "\n Producto: ")
    op = ingr(cad)
    return op

def goodbyeMSG():
    # Mensaje de salida!
    rand = random.randrange(70)
    
    if rand <= 5:
        return "Are you enjoying the time of eve?"

    if rand >5 and rand <= 40:
        return "¡Gracias por venir!"
    
    if rand >40 and rand <= 66:
        return "¡Disfrute su comida!"

    if rand >66:
        return " "

#Ejercicio 15
"""
Ejercicio 15:
El costo de un automóvil nuevo para un comprador es la suma total del 
costo del vehículo, del porcentaje de la ganancia del vendedor y de los impuestos locales 
o estatales aplicables (sobre el precio de venta). Suponer una ganancia del vendedor del 
12% en todas las unidades y un impuesto del 6% y diseñar un algoritmo para leer el costo
total del automóvil e imprimir el costo para el consumidor.
"""

def costoAutomovil():
    costo = ingr("Ingrese el costo del vehiculo $")
    total = costo

    # Gcia del Vendedor
    total += descPerc(costo, 12)

    # Impuestos locales y o estatales
    total += descPerc(costo, 6)
    cad = ("El total del vehiculo es: $" 
        + str(total))

    salida(cad)

#Ejercicio 16
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

#TP4 Sumarized