from flask import Flask
from api.Persona import Persona, PersonaData, PersonaUpdate, PersonaDelete
from flask_restful import Resource, Api
from flask_cors import CORS #para que no haya problemas con las peticiones como por ejemplo usando fetch
                            #tiraba un error asi: Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at http://127.0.0.1:5000/persona. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing)
                            #link de la solucion https://stackoverflow.com/questions/26980713/solve-cross-origin-resource-sharing-with-flask
                            #https://flask-cors.readthedocs.io/en/latest/
app = Flask(__name__)
CORS(app)
api = Api(app)




# Peticion tipo Get que retorna todos los datos de la tabla
api.add_resource(Persona, '/persona')
api.add_resource(PersonaUpdate, '/persona/<persona_codigo>')
api.add_resource(PersonaData, '/personadata/<codigo>')
api.add_resource(PersonaDelete, '/personadelete/<persona_codigo>')


if __name__ == '__main__':
    app.run(port = '5000', debug = True)

# para instalar en mi entorno virtual psycopg2
# pip install psycopg2-binary 