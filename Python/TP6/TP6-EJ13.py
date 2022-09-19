"""
En un circuito eléctrico hay tres interruptores, los cuales pueden estar en 
estado cerrado (1) o abierto (0). Para que un equipo funcione, se requiere que al menos 
dos estén cerrados. Si los datos son el estado de los interruptores, determine si el equipo 
funcionará.
"""
def p_Circuito():
    cir1 = cir2 = cir3 = False
    #cir1 = True
    #cir2 = True
    #cir3 = True
    print("El circuito funcionara") if((cir1 & cir2 == True) or (cir2 & cir3 == True) or (cir1 & cir3 == True)) else print("El circuito no funcionara")

p_Circuito()