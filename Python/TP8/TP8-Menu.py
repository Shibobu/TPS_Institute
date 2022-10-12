"""Menu"""

def menu(op):
    match op:
        case 1: 
            print("Ejercicio con Tuplas: ")
            asig()
        case 2:
            print("Ejercicio con Sets")
            rep()
        case 3: 
            print("Salir")
            return 0
    menu(seleccion("Ingrese la opcion: "))

def seleccion(arg):
    print("------------------\n"
        + "Ingrese 1 para el ejercicio con las tuplas\n"
        + "Ingrese 2 para el ejercicio con Sets\n"
        + "Ingrese 3 para salir: ")
    try:
        op = int(input(arg))
        return op if 0<op<4 else seleccion("Ingrese nuevamente: ")
    except:
        print("No es una cadena!")
        seleccion("Ingrese nuevamente: ")
     

def rep():
  materias = {"Matematicas","Fisica","Quimica","Historia","Lengua"}
  materias.add("Matematicas")
  materias.add("Biologia")
  for i in materias:
    print("Yo estudio {mat}".format(mat= i))

def showlasig(asignaturas):
    for i in asignaturas:
        print("Yo Estudio {asig}".format(asig=i))

def asig():
    asignaturas = ("Matematicas","Fisica","Quimica","Historia","Lengua")
    try: 
        asignaturas[1] = "Biologia"
    except:
        print("Es una tupla no se puede modificar valores! ")
    showlasig(asignaturas)

menu(seleccion("Ingrese un valor: "))