from models.Conexion import Conexion
from models.entities.Persona import Persona

class PersonaModel(Conexion):
    
    def getTable(self):
        self.conectar()
        if self.conectar:
            cursor = self.conexion.cursor()
            sql = "SELECT codigo, nombre, apellido, fecha_nacimiento FROM persona;"
            cursor.execute(sql)  
            personas = []
            for row in cursor:
                persona = Persona(row[0], row[1], row[2], row[3])
                personas.append(persona)
            self.desconectar()   
            return personas
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None

    def insert(self, persona):
        self.conectar()
        if self.conectar:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO persona(nombre, apellido, fecha_nacimiento) VALUES ('%s','%s','%s');"%(persona.nombre, persona.apellido, persona.fecha_nacimiento)
            cursor.execute(sql)
            self.conexion.commit()
            print("Se agrego una persona correctamente")
            self.desconectar() 
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None
    
    def imprimirListaDePersonas(self, personas):
        print(f"Tabla de Personas\n")
        for fila in personas:
            print(f"Nombre: {fila.nombre}, Apellido: {fila.apellido}, Nacimiento: {fila.fecha_nacimiento} \n")
