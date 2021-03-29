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


def msj_help():
    print('\n')
    print('Para más ayuda ejecute python main.py help')
    print('\n')

def resultado_verificacion(resultado,msj):
    if not resultado:
        print('Dump Realizado')
    else:
        print('\n')
        print(msj)
        msj_help()

def main():
    try:
        # obtengo los parametros ingresados si es que hay alguno
        parametros = sys.argv[-1] if len(sys.argv) >= 3 else None

        # en caso de no haber ningun parámetro más que el nombre de la base de datos 
        # y si no esta ingresando el parametro help
        if parametros is None and 'help' not in sys.argv:
            dump = f'pg_dump -U postgres -d {sys.argv[1]} -f dump_{sys.argv[1]}.sql'
            resultado = subprocess.call(shlex.split(dump))
            # msj = 'Dump realizado' if resultado == 0 else 'Error. La base da datos ingresada no existe o tal vez el usuario postgres no tenga permisos necesarios para realizar el dump, pruebe ingresando un usuario despues del parametro python main.py -U [USUARIO] -d [DB_NAME]'
            resultado_verificacion(resultado,'Error. La base da datos ingresada no existe o tal vez el usuario postgres no tenga permisos necesarios para realizar el dump, pruebe ingresando un usuario despues del parametro python main.py -u [USUARIO] -d [DB_NAME]')

        elif '-h' in sys.argv:
            # obtengo el parámetro del host y el posterior del array
            indice_host = sys.argv.index('-h')
            host = sys.argv[ indice_host + 1 ]

            # obtengo el parámetro de usuario y el posterior del array
            indice_usuario = sys.argv.index('-u')
            usuario = sys.argv[indice_usuario + 1]
           
            # obtengo el parámetro de la base de datos y el posterior del array
            indice_db = sys.argv.index('-d') if '-d' in sys.argv else None
            db = sys.argv[indice_db + 1]

            dump = f'pg_dump -h {host} -p 5432 -U {usuario} -d {db} -f dump_{db}.sql'
            resultado = subprocess.call(shlex.split(dump))
            resultado_verificacion(resultado,'Error. El host o usuario incorrectos. Tambien puede ser que la base da datos ingresada no existe.')

        ## en caso de tener el parametro para asignar usuario 
        elif '-u' in sys.argv:
            # obtengo el parámetro de usuario y el posterior del array
            indice_usuario = sys.argv.index('-u')
            usuario = sys.argv[indice_usuario + 1]
           
            # obtengo el parámetro de la base de datos y el posterior del array
            indice_db = sys.argv.index('-d') if '-d' in sys.argv else None
            db = sys.argv[indice_db + 1]
           
            dump = f'pg_dump -U {usuario} -d {db} -f dump_{db}.sql'
            resultado = subprocess.call(shlex.split(dump))
            # msj = 'Dump realizado' if resultado == 0 else 'Error. Usuario incorrecto o la base da datos ingresada no existe.'
            resultado_verificacion(resultado,'Error. Usuario incorrecto o la base da datos ingresada no existe.')

        

        elif 'help' in sys.argv:
            print('\n\t *************** Ayudas ******************\n')
            print('dump de una base de datos suponiendo que el usuario es postgres y estoy en el mismo servidor de la db:')
            print('\tpython main.py [nombre_bd]\n')   
            print('dump de una base de datos ingresando el nombre del usuario y nombre de la base de datos:')
            print('\tpython main.py -u [nombre_usuario] -d [nombre_bd]')  
            print('\n')
        else:
            print('hay parametros')

    except Exception as e:
        print(f'Error: {e} ')
        msj_help()


if __name__ == "__main__":
    main()
else:
    print('Error al ejecutar el script')
