class Persona(object):
    def __init__(self,cedula, nombre, apellido, sexo ):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
    
    def __str__(self):
        return "%s %s,%s %s." %(
            str(self.cedula), self.nombre,
            self.apellido, self.getGenero(self.sexo)
        )
    def hablar(self, mensaje):
        return mensaje

    def getGenero(self, sexo):
        genero = ('Masculino', 'Femenino')
        if sexo == 'M':
            return genero[0]
        elif sexo == 'F':
            return genero[1]
        else:
            return "Desconocido"


persona1 = Persona("V-13458796", "Leonardo", "Caballero", "M")
persona2 = Persona("V-23569874", "Ana", "Poleo", "F")

print(str(persona1))
print(persona2)
print(persona2.getGenero(persona2.sexo))

class Supervisor(Persona):
    
    def __init__(self, cedula, nombre, apellido, sexo, rol):
        Persona.__init__(self, cedula, nombre, apellido, sexo)

        self.rol = rol
        self.tareas = ['10','11', '12', '13']

    def __str__(self):
        return "%s %s, rol: '%s', sus tareas: %s." % (
            self.nombre, self.apellido, 
            self.rol, self.consulta_tareas())

    def consulta_tareas(self):
        return ', ' .join(self.tareas)

