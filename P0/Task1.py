"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

numbers = set()

for text, call in zip(texts, calls):
    for i in range(0, 2):
        numbers.add(text[i])
        numbers.add(call[i])

print(f"There are {len(numbers)} different telephone numbers in the records.")

"""
Calculate Big O
O(n + 2n + 1) n for the first for loop; 2n for the second; 1 for print
"""