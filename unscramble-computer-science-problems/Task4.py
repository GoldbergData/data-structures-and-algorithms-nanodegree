"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

dials = {call[0] for call in calls}
receives = [call[1] for call in calls]
real_people = set()

for text, receive in zip(texts, receives):
    for i in range(0, 2):
        real_people.add(text[i])
    real_people.add(receive)

potential_telemarketers = {call for call in dials if call not in real_people}
potential_telemarketers = sorted(list(potential_telemarketers))

print(f"These numbers could be telemarketers: {potential_telemarketers}")
print(f"Total potential telemarketers: {len(potential_telemarketers)}")
