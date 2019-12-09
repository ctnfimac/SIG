from flask import Flask
from api.Persona import Persona, PersonaData, PersonaUpdate
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

# Peticion tipo Get que retorna todos los datos de la tabla
api.add_resource(Persona, '/persona')
api.add_resource(PersonaUpdate, '/persona/<persona_codigo>')
api.add_resource(PersonaData, '/personadata/<codigo>')

if __name__ == '__main__':
    app.run(port = '5000', debug = True)

# para instalar en mi entorno virtual psycopg2
# pip install psycopg2-binary 