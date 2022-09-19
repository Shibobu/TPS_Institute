"""
Ejercicio 6: 
Escribir una función que pida al usuario que introduzca una frase en la 
consola y una vocal, y después muestre por pantalla la misma frase, pero con la vocal 
introducida en mayúscula.
"""

def ingr_str(arg):
    return str(input(arg))

def comp_vow(v:str):
    vowels = "aeiouAEIOUáéíóú"

    if v.__len__() != 1:
        salida("ERROR, ES UNA CADENA Y NO UNA LETRA")
        return False

    if vowels.__contains__(v):
        return True
    salida("ERROR, NO ES UNA VOCAL")
    return False

def find_str(txt:str,v:str):
    if txt.find(v) < 0:
        salida("NO SE ENCONTRO LA VOCAL")
        return False
    else:
        return True
        
def salida(arg):
    print(arg)

def p_ej6():
    cad = ingr_str("Ingrese una frase: \n")
    v = ingr_str("Ingrese una vocal: \n")

    if comp_vow(v) & find_str(cad,v):
        salida(cad.replace(v,v.upper()))

p_ej6()