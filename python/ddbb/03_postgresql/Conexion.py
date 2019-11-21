
import psycopg2


class Conexion(object):

    def __init__(self):
        self.user = "postgres"
        self.password = "postgres"
        self.host = "127.0.0.1"
        self.port = "5432"
        self.database = "empresa"
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                                user = self.user,
                                password = self.password,
                                host = self.host,
                                port = self.port,
                                database = self.database 
                            )
        except(Exception, psycopg2.Error) as error:
            print("Error mientras se conectaba a postgres", error)

    def desconectar(self):
        if self.conexion:
            Conexion.close()
            print('La conexión con Postgresql se a cerrado')

# mirar acá:
#https://pynative.com/python-postgresql-tutorial/ 