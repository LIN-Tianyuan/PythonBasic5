number_list = [5, 8, 222, 1, 9, 3, 6, 15]


def indexMax(list):
    max_number = list[0]
    for element in list:
        if element >= max_number:
            max_number = element
    # print(number_list.index(max_number))
    return number_list.index(max_number)


number = indexMax(number_list)
print(number)