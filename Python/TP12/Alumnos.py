"""
Se encarga del manejo de alumnos, comparar alumnos, entre otras
"""

def ini_alum(dni,nombre,apellido,telefono,correo):
    alumno = {'Nombre' : nombre,
              'Apellido' : apellido,
              'Telefono' : telefono,
              'Correo' : correo}
    alumnoc = {"Dni": dni,
               "Alumno" : alumno}
    return alumnoc

