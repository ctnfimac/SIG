import sqlite3 as sql

conexion = sql.connect("miDB")

try:
    conexion.execute(
                    """
                    create table articulos(
                        codigo integer primary key AUTOINCREMENT,
                        descripcion text,
                        precio real
                    )    
                    """)
    print("Se creo la tabla articulos")
except sql.OperationalError:
    print('La tabla articulos ya existe')



conexion.close()