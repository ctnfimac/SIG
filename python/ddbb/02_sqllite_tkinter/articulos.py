import sqlite3 as sql

class Articulos:
    def abrir(self):
        conexion = sql.connect("/home/cperalta/Escritorio/practicas/python/ddbb/01_sqlLite/miDB")
        return conexion

    def buscarArticuloPorId(self, datos):
        try:
            myconexion = self.abrir()
            cursor = myconexion.cursor()
            query = "select descripcion, precio from articulos where codigo = ?"
            cursor.execute(query,datos)
            return cursor.fetchone()
        finally:
            myconexion.close()

    def recuperar_todos(self):
        try:
            myconexion = self.abrir()
            cursor = myconexion.cursor()
            query = "select codigo,descripcion,precio from articulos"
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            myconexion.close()

    def agregar(self,articulosNuevos):
        try:
            myconexion = self.abrir()
            query = "insert into articulos(descripcion,precio) values (?,?)"
            myconexion.execute(query,articulosNuevos)
            myconexion.commit()
        finally:
            myconexion.close()

    def eliminar(self,codigoArticulo):
        try:
            myconexion =  self.abrir()
            sentencia = "delete from articulos where codigo = ? "
            myconexion.execute(sentencia,codigoArticulo)
            myconexion.commit()
        finally:
            myconexion.close()

articulos = Articulos()


tabla = articulos.recuperar_todos()
if len(tabla) > 0 :
    for fila in tabla:
        print(fila)
"""
tabla = articulos.consulta("2")
if len(tabla) > 0 :
    for fila in tabla:
        print(fila)
"""
# artNuevos = ("mouse", 100)
# articulos.agregar(artNuevos)
#articulos.eliminar("2")