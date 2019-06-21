"""
 @details: buscar el numero mayor de una lista de 5 numeros
           ingresados por teclado en un array
"""
lista = []
for x in range(5):
    valor = int(input("Ingrese un valor numerico: "))
    lista.append(valor)

mayor = lista[0]

for i in range(1,5):
    if(lista[i] > mayor ):
        mayor = lista[i]

print('el numero mayor es: ', mayor)