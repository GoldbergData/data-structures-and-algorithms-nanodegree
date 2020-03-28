
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def search(lookup, i, j):
    half = (j+i)//2
    if i == j:
        return None
    if sorted_list[half] > lookup:
        return search(lookup, 0, half)
    elif sorted_list[half] < lookup:
        return search(lookup, half, j)
    else:
        return half


print(search(9, 0, len(sorted_list)))