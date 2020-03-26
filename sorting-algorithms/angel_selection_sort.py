import random

l = [random.randint(1, 100) for _ in range(10)]
print(f"Sorting: {l}")


for i in range(len(l)):
    min = i
    for j in range(i, len(l)):
        if l[j] < l[min]:
            min = j
    if i != min:
        l[min], l[i] = l[i], l[min]

print(l)