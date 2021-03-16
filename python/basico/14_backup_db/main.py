# fuente https://recursospython.com/guias-y-manuales/os-shutil-archivos-carpetas/
"""
@brief: Realizar un backup de una base de datos
@details: El backup se hará en la carpeta donde se este ejecutando el script o en
          una ruta especificada por parámetro.
          Opciones que va a poder elegir el usuario:
            1) que se haga el backup de toda la base de datos
            2) que se pueda elegir el usuario
            3) que se pueda elegir el servidor
            4) que solo se haga el backup de una lista de tablas para esto se agregara el
               parámetro -tl y se le pasara la lista de nombres tabla1 tabla2 tabla3
            5) tambien puede ser la opcion de hacer el backup de todas las tablas menos de una/s
               con el parámetro -TL tabla1
          
@referencias: https://www.rafalinux.com/?p=1613
"""

# importo las librerias 
import os, sys, subprocess, shlex


def main():
    try:
        # obtengo los parametros ingresados si es que hay alguno
        parametros = sys.argv[-1] if len(sys.argv) >= 3 else None

        ## en caso de no haber ninguno
        if parametros is None:
            dump = f'pg_dump -U postgres -d {sys.argv[1]} -f dump_{sys.argv[1]}.sql'
            resultado = subprocess.call(shlex.split(dump))
            msj = 'Dump realizado' if resultado == 0 else 'Error. La base da datos ingresada no existe o tal vez el usuario postgres no tenga permisos necesarios para realizar el dump, pruebe ingresando un usuario despues del parametro python main.py -U [USUARIO] -d [DB_NAME]'
            print(msj)
        ## en caso de tener el parametro que asigna base de datos
        elif '-u' in sys.argv:
            print('Ingreso el usuario')
        else:
            print('hay parametros')

    except Exception as e:
        print(f'Error: {e} ')


if __name__ == "__main__":
    main()
else:
    print('Error al ejecutar el script')
