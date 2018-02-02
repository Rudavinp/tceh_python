
"""Функция сортирует список чисел по убыванию"""


def sort_array(some_array):
    result_array = []
    array_1 = some_array[:len(some_array)//2]
    array_2 = some_array[len(array_1):]
    if len(array_1) > 1:
        array_1 = sort_array(array_1)
    if len(array_2) > 1:
        array_2 = sort_array(array_2)
    while len(result_array) != len(some_array):
        if array_1[0] > array_2[0]:
            result_array.append(array_1[0])
            array_1.pop(0)
        else:
            result_array.append(array_2[0])
            array_2.pop(0)
        if not array_1:
            for i in array_2:
                result_array.append(i)
        if not array_2:
            for i in array_1:
                result_array.append(i)
    return result_array



print('finish', sort_array([3, 4, 8 ,1, 5, 0, 22]))


