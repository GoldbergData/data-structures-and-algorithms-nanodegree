import random

l = [random.randint(1, 100) for _ in range(10)]


def swap(list, i, min):
    swap = list[i]
    list[i] = list[min]
    list[min] = swap


for i in range(len(l)):
    min = i
    for j in range(i, len(l)):
        if l[j] < l[min]:
            min = j
    swap(l, i, min)

print(l)