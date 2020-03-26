import random

l = [random.randint(1, 100) for _ in range(10)]
print(f"Sorting: {l}")


for i in range(len(l)):
    j = i
    while j > 0 and l[j] < l[j-1]:
        l[j-1], l[j] = l[j], l[j-1]
        j -= 1


print(l)