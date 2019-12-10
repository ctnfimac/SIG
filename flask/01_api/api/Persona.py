from models.Conexion import Conexion
from flask import jsonify, request
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


    def post(self):
        con = Conexion()
        con.conectar()
        if con.conexion:
            cursor = con.conexion.cursor()
            codigo = request.json['codigo']
            nombre = request.json['nombre']
            apellido = request.json['apellido']
            fecha_nacimiento = request.json['fecha_nacimiento']
            print(f"codigo: {codigo}")
            print(f"nombre: {nombre}")
            print(f"apellido: {apellido}")
            print(f"fecha_nacimiento: {fecha_nacimiento}")
            sql = "INSERT INTO persona(codigo, nombre, apellido, fecha_nacimiento) VALUES ('%s','%s','%s','%s');"%(codigo,nombre, apellido, fecha_nacimiento)
            cursor.execute(sql)
            con.conexion.commit()
            return {'status': 'Nueva Persona agregada'}
            con.desconectar()
        else:
            print("Problemas con la conexión")
            return None

class PersonaUpdate(Resource):
    def put(self, persona_codigo):
        con = Conexion()
        con.conectar()
        if con.conexion:
            cursor = con.conexion.cursor()
            nombre = request.json['nombre']
            apellido = request.json['apellido']
            fecha_nacimiento = request.json['fecha_nacimiento']
            sql = "UPDATE persona SET nombre = '%s', apellido = '%s' , fecha_nacimiento = '%s' WHERE codigo = '%s';"%(nombre, apellido, fecha_nacimiento, persona_codigo)
            cursor.execute(sql)
            con.conexion.commit()
            con.desconectar()
            return { "respuesta": "cambio realizado"}
        else:
            print("Problemas con la conexión")
            return None   
    

class PersonaData(Resource):
    def get(self, codigo):
        con = Conexion()
        con.conectar()
        if con.conexion:
            cursor = con.conexion.cursor()
            sql = "SELECT codigo, nombre, apellido, fecha_nacimiento FROM persona WHERE codigo = '%s' LIMIT 1;"%(codigo)
            cursor.execute(sql)
            personas = []
            columnas = ['codigo','nombre','apellido','fecha_nacimiento']
            for row in cursor:
                personas.append(dict(zip(columnas,[row[0],row[1],row[2],row[3]])))
            resultado =  {'persona': personas}
            con.desconectar()
            return jsonify(resultado)
        else:
            print("Problemas con la conexión")
            return None


class PersonaDelete(Resource):
    
    def delete(self, persona_codigo):
        con = Conexion()
        con.conectar()
        if con.conexion:
            cursor = con.conexion.cursor()
            sql = "DELETE FROM persona WHERE codigo = '%s';"%(persona_codigo)
            cursor.execute(sql)
            con.conexion.commit()
            resultado =  {'respuesta': 'se elimino la persona'}
            con.desconectar()
            return jsonify(resultado)
        else:
            print("Problemas con la conexión")
            return None

# fuentes:
# https://unipython.com/como-hacer-paso-a-paso-una-api-restful-en-flask-con-python/
# https://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php