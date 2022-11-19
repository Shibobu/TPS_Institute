from csv import DictWriter ,DictReader
from time import sleep

def generateCSV(filename , state , dataIn, headername:str):
    
    with open(filename, state) as archive:
        
        fields = headername.split(',')
        file = DictWriter(archive,fieldnames=fields)
        file.writeheader()
        file.writerows(dataIn)

    archive.close()
    return 1

def openCSV(filename : str, state : str):
    
    with open(filename,state) as file:

        ent = list(DictReader(file,delimiter=','))
    file.close

    return ent

def showALL(filename : str, state : str):
    alumnos = openCSV(filename , state )
    i = 1
    for v in alumnos:
        print("{d}º Alumno: \n".format(d=i))
        showData(v)
        i+=1
        sleep(0.1)
        

def showData(alumn):
    print("DNI :",alumn["DNI"] + 
          "\nNombre: ", alumn["Nombre"] +
          "\nApellido: ", alumn["Apellido"] +
          "\nDireccion: ", alumn["Direccion"] +
          "\nTelefono: ", alumn["Telefono"] +
          "\nCorreo_Electronico: ", alumn["Correo_Electronico"] +
          "\nNota_Parcial: ", alumn["Nota_Parcial"])
    print("\n")

def writeTXT(filename,state, prom):
    with open(filename,state) as file:
        file.write("Promedio de notas: " + str(prom))
    file.close