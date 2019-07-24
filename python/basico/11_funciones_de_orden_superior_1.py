"""
@brief:Definir una función de orden superior llamada operar. Llegan como parámetro dos enteros y una función. 
    En el bloque de la función llamar a la función que llega como parámetro y enviar los dos primeros parámetros.
    La función retorna un entero.
@details: estoy probando como son las funciiones de orden superior
"""
def operar(valor1, valor2, fn):
    return fn(valor1, valor2)

def sumar(valor1, valor2):
    return valor1 + valor2


dato1 = 2
dato2 = 5

resultado = operar(dato1, dato2, sumar)

print(f"resultado: {resultado}")

"""
@brief: Declarar una clase que almacene el nombre y la edad de una persona. Definir un método que retorne True o False según si la persona es mayor de edad o no. 
    Esta función debe recibir como parámetro una función que al llamarla pasando la edad de la persona retornará si es mayor o no de edad.
    Tener en cuenta que una persona es mayor de edad en Estados Unidos si tiene 21 o más años y en Argentina si tiene 18 o más años
"""

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def esMayorDeEdad(self,fn):
        return fn(self.edad)


def mayorEnArgentina(edad):
        resultado  = True if edad >= 18 else False
        return resultado

def mayorEnEstadosUnidos(edad):
    resultado  = True if edad >= 21 else False
    return resultado 


persona1 = Persona("christian",9)
resultado = 'si' if persona1.esMayorDeEdad(mayorEnArgentina) == True else 'No'
print(f'{persona1.nombre} es mayor?:  {resultado}')


