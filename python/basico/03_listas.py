"""
 @details: Ingresar por teclado los nombres de 5 personas y 
           almacenarlos en una lista. Mostrar el nombre de 
           persona menor en orden alfabético. 
"""

######
#
# Funciones
#
######
def imprimirLista(lista):
    for i in range(0,len(lista)):
        print('valor: ', lista[i])


def buscoPalabraMenor(lista):
    palabraMenor = lista[0]
    for i in range(1,5):
        if lista[i] < palabraMenor:
            palabraMenor = lista[i]
    return palabraMenor
     

listaDeNombres = []

for i in range(5):
    nombre = input("Igrese un nombre: ")
    listaDeNombres.append(nombre)

print('la palabra menor es: ', buscoPalabraMenor(listaDeNombres))
