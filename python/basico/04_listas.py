"""
 @details: Cargar una lista con 5 elementos enteros. 
           Imprimir el mayor y un mensaje si se repite 
           dentro de la lista (es decir si dicho valor se 
           encuentra en 2 o más posiciones en la lista) 
"""
######
#
# Funciones
#
######

def regresarNumeroMayorYSiSeRepite(lista):
    respuesta = { 
                    "valorMayor": lista[0],
                    "seRepite": False  
                }
    for i in range(1,5):
        if lista[i] > respuesta['valorMayor']:
            respuesta['seRepite'] = False
            respuesta['valorMayor'] = lista[i]
        elif lista[i] == respuesta['valorMayor']:
            respuesta['seRepite'] = True
    return respuesta
     

numeros = []

for i in range(5):
    numero = int(input("ingrese un numero: "))
    numeros.append(numero)

print('el numero mayor es: ' , regresarNumeroMayorYSiSeRepite(numeros)['valorMayor'])
  
msj = 'el valor se repite' if regresarNumeroMayorYSiSeRepite(numeros)['seRepite'] == True else 'el valor no se repite'
print(msj)

