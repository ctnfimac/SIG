
"""
@brief:Eliminar los elementos que tengan un campo vacio "" en un array
@details: uso de filter y lambda
"""

lista_de_frutas = ["sandia","pera","manzana","banana","","melon","frutilla","","","naranja"]


# Forma 1
lista_arreglada = []

for fruta in lista_de_frutas:
    if fruta != "":
        lista_arreglada.append(fruta)

print(lista_arreglada)


# forma 2 con el uso de lambda y el método filter
lista_arreglada_2 = list(filter(lambda fruta: fruta != "",lista_de_frutas))
print(lista_arreglada_2)
