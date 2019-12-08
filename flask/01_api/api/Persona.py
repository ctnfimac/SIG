from models.Conexion import Conexion
from flask import jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class Persona(Resource):
    
    def get(self):
        con = Conexion()
        con.conectar()
        if con.conexion:
            cursor = con.conexion.cursor()
            sql = "SELECT codigo, nombre, apellido, fecha_nacimiento FROM persona;"
            cursor.execute(sql)
            personas = []
            columnas = ['codigo','nombre','apellido','fecha_nacimiento']
            for row in cursor:
                # creo un diccionario entre dos array comprimidos y lo agrego al array personas
                personas.append(dict(zip(columnas,[row[0],row[1],row[2],row[3]])))

            resultado =  {'personas': personas}
            return jsonify(resultado)
            con.desconectar()
        else:
            print("Primero tiene que ejecutar el metodo conectar()")
            return None

# fuentes:
# https://unipython.com/como-hacer-paso-a-paso-una-api-restful-en-flask-con-python/
# https://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php