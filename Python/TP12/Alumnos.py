"""
Se encarga del manejo de alumnos, comparar alumnos, entre otras
"""

def ini_alum(nombre,apellido,telefono,correo):
    alumno = {'Nombre' : nombre,
              'Apellido' : apellido,
              'Telefono' : telefono,
              'Correo' : correo}
    return alumno

def show(alum):
    print("Nombre: {N}\n".format(N = alum["Nombre"]) +
          "Apellido: {A}\n".format(A = alum["Apellido"]) +
          "Telefono: {T}\n".format(T = alum["Telefono"]) +
          "Correo: {C}\n".format(C = alum["Correo"]))