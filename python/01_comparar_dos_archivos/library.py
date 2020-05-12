def build_list(file):
    list_aux = []
    for row in file:
        if row[-1] == "\n":
            list_aux.append(row[:-1])
        else:
            list_aux.append(row)
    return list_aux


def build_list_of_differences(list1, list2):
    list_result = []
    for row in list1:
        if row not in list2:
            list_result.append(row)

    for row in list2:
        if row not in list1:
            list_result.append(row)
    return list_result


def build_list_of_equals(list1, list2):
    list_result = []
    for row in list1:
        if row in list2:
            list_result.append(row)

    # for row in list2:
    #     if row in list1:
    #         list_result.append(row)

    return list_result