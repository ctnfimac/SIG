"""
 @details: Crear y cargar una lista con 5 enteros por teclado. 
           Implementar un algoritmo que identifique el menor 
           valor de la lista y la posición donde se encuentra.
"""


######
#
# Funciones
#
######
def imprimirLista(lista):
    for i in range(0,len(lista)):
        print('valor: ', lista[i])

def buscarNumeroMenor(lista):
    #menor = lista[0]
    resultado = [lista[0],0] # valor, posicion
    for i in range(1,len(lista)):
        if lista[i] < resultado[0]:
            resultado[0] = lista[i]
            resultado[1] = i
    return resultado



######
#
# Cuerpo del programa
#
######
listaDeNumeros = []

# ingreso valores
for i in range(5):
    valor = int(input('ingrese un numero: '))
    listaDeNumeros.append(valor)

#imprimirLista(listaDeNumeros)
print('El numero menor es: ', buscarNumeroMenor(listaDeNumeros)[0])
print('Y su posicion es: ', buscarNumeroMenor(listaDeNumeros)[1])




