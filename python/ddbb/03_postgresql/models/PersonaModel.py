from models.Conexion import Conexion

class PersonaModel(Conexion):
    def getTable(self):
        if self.conectar:
            cursor = self.conexion.cursor()
            sql = "SELECT codigo, nombre, apellido, fecha_nacimiento FROM persona;"
            cursor.execute(sql)  
            return cursor
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None

    def insert(self, person):
        if self.conectar:
            cursor = self.conexion.cursor()
            sql = "INSERT INTO persona(nombre, apellido, fecha_nacimiento) VALUES ('zahira','peralta','2009-03-08');"
            cursor.execute(sql)
            self.conexion.commit()
            print("Se agrego una persona correctamente")
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None