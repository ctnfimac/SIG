from models.Conexion import Conexion
from models.entities.Persona import Persona

class PersonaModel(Conexion):
    
    def getTable(self):
        self.conectar()
        if self.conexion:
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
        if self.conexion:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO persona(codigo, nombre, apellido, fecha_nacimiento) VALUES ('%s','%s','%s','%s');"%(persona.codigo,persona.nombre, persona.apellido, persona.fecha_nacimiento)
            cursor.execute(sql)
            self.conexion.commit()
            print("Se agrego una persona correctamente")
            self.desconectar() 
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None
    
    def buscoPersonaPorCodigo(self, codigo):
        self.conectar()
        if self.conexion:
            cursor = self.conexion.cursor()
            sql = "SELECT codigo, nombre, apellido, fecha_nacimiento FROM persona WHERE codigo = '%s' LIMIT 1;"%(codigo)
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

    def eliminarPersonaPorCodigo(self, codigo):
        personaEliminada = self.buscoPersonaPorCodigo(codigo)
        if personaEliminada:
            self.conectar()
            if self.conexion:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM persona WHERE codigo='%s';"%(codigo)
                cursor.execute(sql)
                self.conexion.commit()
                self.desconectar()
                return personaEliminada
            else:
                print("Primero tiene que ejecutar el metodo conectar()")
                return None
        else:
            return False
        

    def imprimirListaDePersonas(self, personas):
        print(f"Tabla de Personas\n")
        for fila in personas:
            print(f"Nombre: {fila.nombre}, Apellido: {fila.apellido}, Nacimiento: {fila.fecha_nacimiento} \n")
