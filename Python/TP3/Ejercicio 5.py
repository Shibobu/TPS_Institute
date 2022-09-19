"""
Ejercicio 5:
Escribir un programa que funcione como un examen tipo múltiple de Choice.
Pregunte al usuario: “¿Qué color se genera mezclando azul y amarillo?”
y muestre las opciones “
1‐Rojo; 
2‐ Violeta; 
3‐ Verde; 
4‐ Negro” 
Luego de recibida la respuesta muestre el mensaje de “Respuesta Correcta”
o “Respuesta incorrecta” según corresponda. (Utilice la estructura 
Según ‐ de Selección Múltiple)
"""

print("Elija la opcion correcta: \n"
    + " ¿Que color se genera mezclando azul y amarillo?"
    + "\n1‐ Rojo" 
    + "\n2‐ Violeta"  
    + "\n3‐ Verde;" 
    + "\n4‐ Negro")
op = int(input())

match op:
    case 3: 
        print("Respuesta correcta!")
    case 1:
        print("Yomama")
    case default: 
        print("Respuesta Incorrecta!")
        
