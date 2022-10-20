"""
Ejercicio 3: Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir
listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una
opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe
volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las
opciones 1 ó 2 se imprimirá un texto cualquiera. Si elige la opción 3, se interrumpirá la
impresión del menú y el programa finalizará.
"""

def ing_opc(arg):
    try: 
        x = int(input(arg))
        return x
    except: 
        print("Error de ingreso, ingrese nuevamente:")
        return 0

def menu():
    print("Seleccione una opcion: \n"
        + "1---------Comenzar el programa \n"
        + "2---------Imprimir listado \n"
        + "3---------Finalizar el programa \n")
    op = ing_opc("Ingrese una opcion: ") 
    return op if op != 0 else menu()

def seleccion(op):
    match(op):
        case 1: 
            print("Acchi Kocchi")
        case 2:
            print("Doki Doki Waku Waku")
        case 3:
            print("Salir")
            return 0
        case _:
            print("Opcion no existente, porfavor ingrese nuevamente")
    return -1

def p_menu():
    
    while seleccion(menu()) !=  0:
        continue

p_menu()
    