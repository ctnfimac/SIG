"""
 @details:  Desarrollar una aplicación que nos permita crear un diccionario 
            ingles/castellano. La clave es la palabra en ingles y el valor es 
            la palabra en castellano.
    Crear las siguientes funciones:
    1) Cargar el diccionario.
    2) Listado completo del diccionario.
    3) Ingresar por teclado una palabra en ingles y si existe en el diccionario 
    mostrar su traducción
"""
######
#
# Funciones
#
######

def cargarDiccionario():
    diccionario = {
        'orange':'naranja',
        'apple':'manzana',
        'pen':'lapicera'
        }
    """for i in range(2):
        clave = input('ingrese la palabra en ingles: ')
        valor = input('ingrese su traduccion al castellano: ')
        diccionario[clave] = valor"""
    return diccionario

def imprimirDiccionario(diccionario):
    for clave in diccionario:
        print(f"{clave}:{diccionario[clave]}")

def buscarYtraducirPalabra(diccionario):
    palabra = input('ingrese que palabra quiere traducir:').lower()
    respuesta = 'la palabra no existe' if diccionario.get(palabra) == None else diccionario.get(palabra)
    return respuesta #diccionario.get(palabra)


diccionario = cargarDiccionario()
imprimirDiccionario(diccionario)

print()

print('La traduccion es:', buscarYtraducirPalabra(diccionario))

