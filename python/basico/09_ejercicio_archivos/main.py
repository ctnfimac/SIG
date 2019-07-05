"""
 @brief: manipulacion de archivos
 @details:
    realizar un programa que mediante un archivo el cual tiene una consulta, remplazar los tres
    valores del select por los datos proporcionados y generar un archivo nuevo con el nombre usando
    esos 3 datos, ejemplo:
    tengo un archivo llamado query_christianperalta_programador.sql
    y la siguiente consulta adentro:
    select * from tabla
    where nombre = 'christian' , apellido = 'peralta' , profesion = 'programador'
    order by fecha asc;

    tengo un dato el cual es:
    [
        {
        'nombre':'zahira',
        'apellido':'peralta',
        'profesion':'ladrar'
        }
    ]

    entonces tengo que generar un archivo que se llame query_zahiraperalta_ladrar.sql
    y adentro la query tiene que ser
    select * from tabla
    where nombre = 'zahira' , apellido = 'peralta' , profesion = 'ladrar'
    order by fecha asc;
    se van a generar la cantidad de archivos dependiento la cantidad de info que haya en los datos
"""
from funciones import sacar_espacios, eliminarTildes, generoLosTitulosDeLosArchivos
from datos import informacionNormalizada,informacionOriginal
import shutil
from itertools import *



## leo archivo
archivoLeido = open('origen/query_christianperalta_programador.sql', encoding="utf-8")

## leo primera linea
linea = archivoLeido.readline()

filaBuscada = ''
listaDeFilas = []

while linea != '':
    listaDeFilas.append(linea)
    linea = archivoLeido.readline()

for linea in listaDeFilas:
    if 'dia' in linea and 'franja_hora' in linea and 'filtro' in linea:
        filaBuscada = eliminarTildes(linea)

textoIterable = chain(filaBuscada)
textoIterable2 = chain(filaBuscada)


posiciones = [] # acá guardo las posiciones en donde se encuentran las comillas '
                # van a ser 6 posiciones

# recorro el texto iterable y guardo las posiciones de las comillas simples
posicion = 0

for letra in textoIterable:
    if letra == "'":
        posiciones.append(posicion + 1)
    posicion = posicion + 1


# recorro el texto iterable y guardo las letras desde la primer comillas
# hasta la segunda y asi con las otras dos
posicion = 0
diccionario = {"dia":[], "franja_hora":[], "filtro":[]}
activoPrimerPalabra = False
activoSegundaPalabra = False
activoTerceraPalabra = False


for letra in textoIterable2:
    if posicion == posiciones[0]:
        activoPrimerPalabra = True
    if posicion == posiciones[1] :
        activoPrimerPalabra = False
    if activoPrimerPalabra == True :
        diccionario["dia"].append(letra) 

    if posicion == posiciones[2]:
        activoSegundaPalabra = True
    if posicion == posiciones[3] :
        activoSegundaPalabra = False
    if activoSegundaPalabra == True :
        diccionario["franja_hora"].append(letra) 

    if posicion == posiciones[4]:
        activoTerceraPalabra = True
    if posicion == posiciones[5] :
        activoTerceraPalabra = False
    if activoTerceraPalabra == True :
        diccionario["filtro"].append(letra)        
    posicion = posicion + 1


# saco la ultima posicion de las listas
diccionario["dia"].pop()
diccionario["franja_hora"].pop()
diccionario["filtro"].pop()

# convierto los tres vectores en strings, saco los espacios y convierto a minuscula
dia = sacar_espacios(''.join(diccionario["dia"])).lower()
franja_hora = sacar_espacios(''.join(diccionario["franja_hora"])).lower()
filtro = sacar_espacios(''.join(diccionario["filtro"])).lower()

"""
print(dia)
print(franja_hora)
print(filtro)
"""

# concateno el dia - franja hora - filtro para obtener el titulo del archivo
titulo = "indice_circulacion_" + filtro + "_" + dia + "_" + franja_hora + "_caba_3857.map"


# el archivo leido lo copio en otra carpeta
#shutil.copy('origen/indice_de_circulacion_enero2019-abril2019_sabado_16a20_caba_3857.map','destino/'+titulo)


# cierro la instancia
archivoLeido.close()


mistitulos = generoLosTitulosDeLosArchivos(informacionNormalizada)
#print(mistitulos)
print(len(mistitulos))

#for titulo in mistitulos:
#    shutil.copy('origen/prueba.sql','destinop/'+ titulo)


# leer el archivo y reemplazar las palabras
archivoLeido = open('origen/info.sql', encoding="utf-8")
shutil.copy('origen/info.sql','destino/pruebacopia.sql')

# prueba para reemplazar una palabra por otra en un archivo
f2 = open('destino/pruebacopia.sql', 'w')
for line in archivoLeido:
    f2.write(line.replace('campo1', 'dasdingo'))
archivoLeido.close()
f2.close()
