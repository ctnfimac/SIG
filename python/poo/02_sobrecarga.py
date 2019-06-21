"""
 @details:  Desarrollar una clase llamada Lista, que permita pasar al método 
           __init__ una lista de valores enteros.
           Redefinir los operadores +,-,* y // con respecto a un valor entero 
"""


class Lista(object):

    def __init__(self,lista):
        self.lista = lista
    """
    def __add__(self,numero):
        nueva = []
        for i in range(len(self.lista)):
            nueva.append(self.lista[i] + numero)
        return nueva
    """
    def __add__(self,numeros):
        nueva = []
        for i in range(len(self.lista)):
            nueva.append(self.lista[i] + numeros[i])
        return nueva

    def __sub__(self,numeros):
        nueva = []
        for i in range(len(self.lista)):
            nueva.append(self.lista[i] - numeros[i])
        return nueva

    def __mul__(self,numeros):
        nueva = []
        for i in range(len(self.lista)):
            nueva.append(self.lista[i] * numeros[i])
        return nueva

    def __floordiv__(self,numeros):
        nueva = []
        for i in range(len(self.lista)):
            nueva.append(self.lista[i] / numeros[i])
        return nueva

    def imprimir(self):
        print(self.lista)

lista = Lista([1,3,5,6])
print(lista + [3,3,4,5])
print(lista - [3,3,4,5])
print(lista * [3,3,4,5])
print(lista // [1,3,4,5])