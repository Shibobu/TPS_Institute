"""
Ejercicio 7: Escribir una función que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco 
enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.
"""
def ingint(arg):
    return int(input(arg))

def ing_list(list):
    for i in range(5):
        list.append(ingint("Ingrese un valor: "))

def sum_list(list1,list2):
    sum = []
    for i in range(5):
        sum.append(list1[i] + list2[i])
    return sum

def show_list(l1,arg):
    print(arg)
    j = 1
    for i in l1:
        print(str(j) + ")\t",i)
        j+=1

def p_sum_List():
    list1 = []
    list2 = []
    list3 = []
    print("Ingrese la primera lista: ")
    ing_list(list1)
    print("Ingrese la segunda lista: ")
    ing_list(list2)
    list3 = sum_list(list1,list2)
    show_list(list1, "Lista 1: ")
    show_list(list2, "Lista 2: ")
    show_list(list3, "Suma de lista 1 y lista 2: ")

p_sum_List()