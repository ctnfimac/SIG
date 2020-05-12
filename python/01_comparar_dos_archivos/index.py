from library import *

file1 = open("file1.txt","r")
file2 = open("file2.txt","r")
output = open("output.txt","w")
output_equals = open("list_equals.txt","w")

list_file1 = build_list(file1)
list_file2 = build_list(file2)
list_result = build_list_of_differences(list_file1, list_file2)
list_result_equals = build_list_of_equals(list_file1, list_file2)

# join lo que hace es concatenar cada elemento de la lista convertido a string con \n
# a partir del primer string o sea, dato1 + \n , dato2 + \n etc..
output.write("\n".join([str(elemento) for elemento in list_result]))
output_equals.write("\n".join([str(elemento) for elemento in list_result_equals]))

file1.close()
file2.close()
output.close()




