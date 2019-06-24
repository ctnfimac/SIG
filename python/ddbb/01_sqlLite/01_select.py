import sqlite3 as sql

conexion = sql.connect("miDB")


# obtengo todas las filas de la tabla  
tabla = conexion.execute("SELECT * FROM articulos")

for fila in tabla:
    print(f"id: {fila[0]}, descripcion: {fila[1]}, precio: {fila[2]}")


# Ahora obtengo una sola fila 
codigo = int(input("ingrese el codigo del articulo a a buscar: "))
tabla = conexion.execute( """
                            SELECT * 
                            FROM articulos 
                            WHERE codigo = ?
                          """
                         ,(codigo,))
fila = tabla.fetchone()

if fila != None:
    print(f"Articulo buscado: {fila}")
else:
    print('No existe articulo con dicho codigo')


# Ahora recupero varias filas de la tabla
precio = int(input("ingrese un precio: "))
tabla = conexion.execute("""
                            SELECT * 
                            FROM articulos
                            WHERE precio > ?
                         """
                         ,(precio,))

filas = tabla.fetchall()

print(f"los productos con un precio mayor a {precio} son:")
if len(filas) > 0:
    for fila in filas:
        print(fila)
else:
    print("No existen productos con un precio mayor al ingresado")

conexion.close()