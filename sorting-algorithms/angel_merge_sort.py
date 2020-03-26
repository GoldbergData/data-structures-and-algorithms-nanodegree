import random

l = [5,4,3,2,1]#[random.randint(1, 100) for _ in range(10)]
print(f"{l}")

#1. Split in half
#2. Recursively merge each half
#3. Merge each sorted half together

def merge_sort(list):
    half = len(list)//2
    left, right = list[:half], list[half:]

    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)

    rval = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            rval.append(left[i])
            i += 1
        else:
            rval.append(right[j])
            j += 1
    if i < len(left):
        rval = [*rval, *left[i:]]
    else:
        rval = [*rval, *right[j:]]

    return rval


print(merge_sort(l))