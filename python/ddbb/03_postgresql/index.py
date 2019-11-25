
from models.PersonaModel import PersonaModel
from models.entities.Persona import *

##
# bloque en el que muestro todos las personas de la tabla
###

persona = PersonaModel()
tablaDePersonas = persona.getTable()
persona.imprimirListaDePersonas(tablaDePersonas)



##
# bloque en el que agrego una persona nueva
###

persona = PersonaModel()
personaNueva = Persona('','Sasha','Diaz','2015-12-12')
persona.insert(personaNueva)
