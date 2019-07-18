import re

# indica que tengo que poner si o si 5 dígitos
# y que tengan valores del 1 al 5
patron1 = re.compile('[1-5]{5}')
print('patron1: ' , patron1.match('23421'))



# indica que tengo que poner si o si 3 dígitos
# y que tengan valores del 1 al 5
patron2 = re.compile('-[5-9]{3}')
print('patron2: ' , patron2.match('-678'))



# indica que tengo que poner cualquier caracter
# que no sea igual a: a,b,z
patron3 = re.compile('[^abz]')
print('patron3: ' , patron3.match('p'))


# coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
patron4 = re.compile('a[3-5]+') 
print('patron4: ' , patron4.match('a4'))