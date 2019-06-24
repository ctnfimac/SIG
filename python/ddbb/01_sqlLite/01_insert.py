import sqlite3 as sql

conexion = sql.connect("miDB")

conexion.execute("INSERT INTO articulos(descripcion, precio) values(?,?)",("Ram",2000))
conexion.execute("INSERT INTO articulos(descripcion, precio) values(?,?)",("Monitor",5000))
conexion.execute("INSERT INTO articulos(descripcion, precio) values(?,?)",("PC Gammer",90000))


conexion.commit()
conexion.close()
