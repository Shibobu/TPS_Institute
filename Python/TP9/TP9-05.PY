"""
Ejercicio 5: Escribir una función que muestre la sumatoria de todos los múltiplos de 3 
encontrados entre el 0 y el 100.
"""
def multiplo(pd):
    while pd % 3 != 0:

            pd +=1
    return pd

def sumatoria():
    sum = 0
    pd = 1
    while pd < 100:
        pd = multiplo(pd)
        sum += pd
        pd += 1

    print ("La sumatoria de los multiplos de 3 entre 0 y 100 es:", sum)
    
if __name__ == "__main__":
    sumatoria()