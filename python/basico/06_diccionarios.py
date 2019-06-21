"""
 @details:  Crear un diccionario en Python que defina como clave el número de 
            documento de una persona y como valor un string con su nombre.
            Desarrollar las siguientes funciones:
            1) Cargar por teclado los datos de 4 personas.
            2) Listado completo del diccionario.
            3) Consulta del nombre de una persona ingresando su número de 
               documento. 
"""
######
#
# Funciones
#
######

def cargarDiccionario():
    diccionario = {} 
    for i in range(4):
        documento = input('ingresar documento:')
        nombre = input('ingresar nombre: ')
        diccionario[documento] = nombre
    return diccionario

def imprimirDiccionario(diccionario):
    for clave in diccionario:
        print(f"{clave}:{diccionario[clave]}")

def consularPersona(diccionario):
    documento = input('consultar nombre de la persona de documento numero:')
    respuesta = 'No existe la persona con el documento ingresado' if diccionario.get(documento) == None else diccionario.get(documento)
    return respuesta 


personas = cargarDiccionario()
imprimirDiccionario(personas)
print('la persona buscada es:',consularPersona(personas))