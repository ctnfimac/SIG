from library import *
from const import *

# Abro los archivos
file1 = open(ARCHIVO1,"r")
file2 = open(ARCHIVO2,"r")
output_diff = open(ARCHIVO_DATOS_DISTINTOS,"w")
output_equals = open(ARCHIVO_DATOS_IGUALES,"w")


# Construyo los array de datos a partir de los dos archivos a comparar
list_file1 = build_list(file1)
list_file2 = build_list(file2)


list_result = build_list_of_differences(list_file1, list_file2)
list_result_equals = build_list_of_equals(list_file1, list_file2)

# join lo que hace es concatenar cada elemento de la lista convertido a string con \n
# a partir del primer string o sea, dato1 + \n , dato2 + \n etc..
output_diff.write("\n".join([str(elemento) for elemento in list_result]))
output_equals.write("\n".join([str(elemento) for elemento in list_result_equals]))



# Cierro los archivos
file1.close()
file2.close()
output_diff.close()
output_equals.close()




