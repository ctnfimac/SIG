
from models.PersonaModel import PersonaModel
from models.entities.Persona import *

##
# bloque en el que muestro todos las personas de la tabla
###
"""
persona = PersonaModel()
tablaDePersonas = persona.getTable()
persona.imprimirListaDePersonas(tablaDePersonas)
"""


##
# bloque en el que agrego una persona nueva
###
"""
persona = PersonaModel()
personaNueva = Persona('','Sasha','Diaz','2015-12-12')
persona.insert(personaNueva)
"""


##
# Busco una persona ingresando su codigo
###

persona = PersonaModel()
codigo = 7
personaBuscada = persona.buscoPersonaPorCodigo(codigo)
persona.imprimirListaDePersonas(personaBuscada)


##
# Eliminar una persona ingresando su codigo
###


persona = PersonaModel()
codigoDeLaPersonaAeliminar = 1
personaEliminada = persona.eliminarPersonaPorCodigo(codigoDeLaPersonaAeliminar)
if personaEliminada:
    print("Persona eliminada")
    persona.imprimirListaDePersonas(personaEliminada)
else: print("No se eliminó ninguna persona")
