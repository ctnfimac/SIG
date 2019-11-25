
from models.PersonaModel import PersonaModel

##
# bloque en el que muestro todos las personas de la tabla
###
persona = PersonaModel()
persona.conectar()
tablaDePersonas = persona.getTable()
print(f"Tabla de Personas\n")
for fila in tablaDePersonas:
    print(f"Nombre: {fila[1]}, Apellido: {fila[2]}, Nacimiento: {fila[3]} \n")
persona.desconectar()


##
# bloque en el que agrego una persona nueva
###
persona = PersonaModel()
persona.conectar()
persona.insert("dato")
persona.desconectar()