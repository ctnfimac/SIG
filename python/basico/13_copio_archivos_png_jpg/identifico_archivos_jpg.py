# fuente https://recursospython.com/guias-y-manuales/os-shutil-archivos-carpetas/
"""
@brief: identificar los archivos .jpg o .png en una determinada carpeta
@details: se puede ingresar la ruta de la carpeta por parámetro, de no ser asi ejecuta el programa en
          la carpeta actual, identifico todos los archivos .jpg y .png de un directorio, los copio y pego 
          en un directorio nuevo el cual tendra el nombre de fotos_[FECHA_ACTUAL]{_xx} el xx es por si se crea
          la misma carpeta en el mismo día
@referencias: https://recursospython.com/guias-y-manuales/os-shutil-archivos-carpetas/ 
              https://www.programiz.com/python-programming/datetime/current-datetime
"""

import os, sys, shutil
from datetime import date


def main():

    # compruebo si se ingrso una ruta especifica de directorio o no
    if len(sys.argv) >= 2:

        # Obtengo el valor ingresado como parámetro por consola
        path = sys.argv[1]
 
        try:
            # Verifico que dicho path existe y listo sus archivos y carpetas
            lista_de_datos = os.listdir(path)

            # Obtengo el nombre de todos los archivos en el directorio que tengan la extensión .png y .jpg
            lista_de_jpg_png = list(filter(lambda dato: '.jpg' in dato or '.png' in dato, lista_de_datos))

            # Si no hay ninguno muestro un mensaje diciendo que no hay ningun archivo con esa extension
            if len(lista_de_jpg_png) == 0:
                print('No hay archivos .png o .jpg en el directorio')
            else:

                # Si hay alguno entonces creo una carpeta con el nombre correspondiente
                # para esto obtengo todas las carpetas que tengan en su nombre el valor de la fecha actual
                # en caso de haber 2 entonces mi carpeta va a tener el nombre fotos_[FECHA_ACTUAL]_03
                fecha_actual = date.today()
                fecha = fecha_actual.strftime("%d_%m_%Y")

                carpetas_a_fecha_actual = list(filter(lambda dato: fecha in dato,lista_de_datos))

                if len(carpetas_a_fecha_actual) >= 1:
                    # obtengo los indices 
                    lista_de_indices = sorted(list(map(lambda dato: int(dato.split('_')[-1]), carpetas_a_fecha_actual)))
                    
                    # genero el nombre de mi carpeta
                    nombre = 'fotos_' + fecha + '_0' + str(lista_de_indices[-1] + 1) if lista_de_indices[-1] >= 0 and lista_de_indices[-1] < 9  else 'fotos_' + fecha + '_' +str(lista_de_indices[-1] + 1)
                    
                    # creo la carpeta que contendra las imagenes 
                    os.mkdir(path + '/' + nombre)

                    # copio las imagenes en la carpeta creada
                    for imagen_name in lista_de_jpg_png:   
                        shutil.copy(imagen_name, path+'/'+nombre)

                   
                else:
                    nombre = 'fotos_' + fecha + '_01'
                    os.mkdir(path + '/' + nombre)

                    for imagen_name in lista_de_jpg_png:   
                        shutil.copy(imagen_name,path + '/' + nombre)

                # Informo cuantas imagenes fueron copiadas
                print(f'Fueron copiados {len(lista_de_jpg_png)} archivos')

        except FileNotFoundError as e:
            print('Error.No existe el directorio ingresado')
            print(f'Detalle del error: {e.__str__()}')
    else:
        print('no ingreso ruta de la carpeta')




# Compruebo si estoy ejecutando el script desde este archivo u otro
# en caso de ser otro mando un mensaje diciendo que no puede ejecutarse
if __name__ == "__main__":
    main()
else:
    print('Error al querer ejecutar el script')











