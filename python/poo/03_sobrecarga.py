"""
 @details:  Plantear una clase Rectangulo. Definir dos atributos 
            (ladomenor y ladomayor). Redefinir el operador == de 
            tal forma que tengan en cuenta la superficie del rectángulo. 
            Lo mismo hacer con todos los otros operadores relacionales.
"""

class Rectangulo(object):

    def __init__(self,ladoMayor, ladoMenor):
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def superficie(self):
        return self.ladoMayor * self.ladoMenor

    def __eq__(self, rectangulo):
        return self.superficie() == rectangulo.superficie()

    def __le__(self, rectangulo):
        if self.superficie() <= rectangulo.superficie():
            return True
        else: return False 

rectangulo1 = Rectangulo(11,20)
rectangulo2 = Rectangulo(20,11)

msj = 'son iguales' if rectangulo1 == rectangulo2 else 'son distintos'
print(msj)

msj = 'rectangulo1 es menor o igual que rectangulo2' if rectangulo1 <= rectangulo2 else 'rectangulo1 es NO menor o igual que rectangulo2'
print(msj)