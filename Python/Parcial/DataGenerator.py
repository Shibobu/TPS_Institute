"""
Data Generation
"""

from random import randint , choice

def genDNI():
    retSTR = ""
    for i in range(8):

        if i < 2:

            retSTR += str(randint(0,6)) 
        else:
            
            retSTR += str(randint(1,9))
    return retSTR

def genPick(ks):
    return choice(ks)

def genNombre():
    namelist = ["Gonzalo", "Jesus" , "Guillermo", "Ana", "Luciana", "Mateo", "Sofia", "Matias", "Pedro"]
    return genPick(namelist)

def genApellido():
    apelist = ["Zuleta", "Gimenez", "Ochoa", "Perez", "Gutierrez", "Zapata", "Esquival","Marinera","Tavera"]
    return genPick(apelist)

def gendireccion():
    dirId = ["Av.","Pje.",""]
    direc=["Santiago del Estero", "Ituzaingo", "Güemes", "Saltadilla", "Cordoba", "Buenos Aires", "Paraguay", "San Martin"]
    dirNum = randint(1,1000)

    retStr  = genPick(dirId) + genPick (direc) + " Nro: " + str(dirNum)
    return retStr
 
def genTelefono():
    codArea = randint(0,399)
    tf = ""

    for i in range(7):

        if i == 1 :
            tf += str(randint(5,6))
        else:
            tf += str(randint(0,9))
    
    return str(codArea)+ "-" + tf

def genCorreo():
    corrPX = ["@gmail.com","@yahoo.com", "@hotmail.com", "@fulanitoXpress.tv", "@live.com.ar"]
    correo = ["ganzadasal","pepemcapo", "boquitaelmasgrandepapa", "cocinerosasoc", "manzana231",
             "doommy", "seekgod","awawa","squidalde_squidoodle","yourdnoodle","stopme"]

    return genPick(correo)+genPick(corrPX) 

def genNota():
    return randint(1,100)

def genCompl():
    alumno = {
        'DNI': genDNI(),
        'Nombre': genNombre(),
        'Apellido': genApellido(),
        'Direccion': gendireccion(),
        'Telefono': genTelefono(),
        'Correo_Electronico' : genCorreo(),
        'Nota_Parcial': genNota()
    }
    return alumno