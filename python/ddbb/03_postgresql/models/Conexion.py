
from abc import abstractclassmethod, ABCMeta
import psycopg2
import Config

class Conexion(metaclass=ABCMeta):

    def __init__(self):
        self.user = Config.USER_DB_SERVER 
        self.password = Config.PASSWORD_DB_SERVER
        self.host = Config.IP_DB_SERVER
        self.port = Config.PORT_DB_SERVER
        self.database = Config.DB_NAME
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

    @abstractclassmethod
    def getTable(self):
        pass

    
    @abstractclassmethod
    def insert(self,object):
        pass

    @abstractclassmethod
    def buscoPersonaPorCodigo(self, codigo):
        pass

    @abstractclassmethod
    def eliminarPersonaPorCodigo(self, codigo):
        pass

    @abstractclassmethod
    def modificarPersona(self,persona):
        pass

    def desconectar(self):
        if self.conexion:
            self.conexion.close()
            #print('La conexión con Postgresql se a cerrado')

# mirar acá:
#https://pynative.com/python-postgresql-tutorial/ 

      


