import random

def selection_sort(array):
    """

    :param array: a list data structure
    :return: a sorted array
    """

    min_value = array[0]
    min_found = False

    for i, _ in enumerate(array[:-1]):
        j_array = array[i + 1:]
        for j, _ in enumerate(j_array):
            if j_array[j] < min_value:
                min_value = j_array[j]
                min_value_index = i + j + 1
                min_found = True

        if min_found:
            swap_value = array[i]
            array[i] = min_value
            array[min_value_index] = swap_value
            min_value = j_array[0]
            min_found = False
        else:
            min_value = j_array[0]

    return array


test_array = [2, 5, 10, 8, 15, 3]
test_array_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
test_array_3 = [2, 6, 3, 2, 4]

test_array_4 = [random.randint(1, 100) for _ in range(10)]


selection_sort(test_array)
selection_sort(test_array_2)
selection_sort(test_array_3)
selection_sort(test_array_4)
