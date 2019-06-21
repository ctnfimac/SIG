"""
 @details:  Se desea almacenar los datos de 3 alumnos. Definir un diccionario 
            cuya clave sea el número de documento del alumno. Como valor 
            almacenar una lista con componentes de tipo tupla donde almacenamos 
            nombre de materia y su nota.

Crear las siguientes funciones:
1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las 
    materias y sus notas)
2) Listado de todos los alumnos con sus notas
3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas. 
"""
######
#
# Funciones
#
######

def cargarAlumnos():
    alumnos = {}
    contador = 0
    while contador != 3:
        dni = input('Ingrese su dni: ')
        materia = input('Ingrese el nombre de la materia: ')
        nota = int(input('Ingrese la nota: '))
        alumnos[dni] = (materia,nota) 
        contador = contador + 1 
    return alumnos

def imprimirAlumnos(diccionario):
    for clave in diccionario:
        print(f"dni: {clave}, materia: {diccionario[clave][0]}, nota:{diccionario[clave][1]}")


def consultarAlumnoPorDni(diccionario):
    dni = input('Ingrese el dni del alumno a buscar: ')
    if dni in diccionario:
        print(f"dni: {dni}, materia: {diccionario[dni][0]}, nota: {diccionario[dni][1]}")


######
#
# Main
#
######
alumnos = cargarAlumnos()
imprimirAlumnos(alumnos)
consultarAlumnoPorDni(alumnos)