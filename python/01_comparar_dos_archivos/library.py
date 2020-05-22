"""
@brief: Construyo un array a partir de los datos contenidos en 
        un archivo dichos datos son cadenas que ocupan
"""
def build_list(file):
    list_aux = []
    for row in file:
        if row[-1] == "\n":
            list_aux.append(row[:-1])
        else:
            list_aux.append(row)
    return list_aux


"""
@brief: construye una lista con los valores que difieren
        entre dos listas
"""
def build_list_of_differences(list1, list2):
    # elimino los espacios en blanco de cada fila
    list1 = list(map(lambda x: x.strip(), list1))
    list2 = list(map(lambda x: x.strip(), list2))

    list_result = []

    # Recorro la list1 y verifico que elementos no estan 
    # en la list2, aquellos que no lo estan lo guardo en
    # el array list_result
    for row in list1:
        if row not in list2:
            list_result.append(row)

    # Recorro la list2 y verifico que elementos no estan 
    # en la list1, aquellos que no lo estan lo guardo en
    # el array list_result
    for row in list2:
        if row not in list1:
            list_result.append(row)
    return list_result




"""
@brief: construye una lista con los valores que son iguales
        entre dos listas
"""
def build_list_of_equals(list1, list2):
    # elimino los espacios en blanco de cada fila
    list1 = list(map(lambda x: x.strip(), list1))
    list2 = list(map(lambda x: x.strip(), list2))

    list_result = []
    
    # Recorro la list1 y verifico que elementos estan 
    # en la list2, aquellos que coinciden lo agrego en
    # el array list_result
    for row in list1:
        if row in list2:
            list_result.append(row)

    return list_result