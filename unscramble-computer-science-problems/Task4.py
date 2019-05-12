"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import pandas as pd

with open('unscramble-computer-science-problems/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('unscramble-computer-science-problems/calls.csv', 'r') as f:
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

dialed = set([call[0] for call in calls])

text_numbers = []
for text in texts:
    text_numbers.append(text[0])
    text_numbers.append(text[1])

received = [call[1] for call in calls]

maybe_not_tele_mkt = set(zip(text_numbers, received))

potential_telemarketers = [call for call in dialed if call not in maybe_not_tele_mkt]

potential_telemarketers = sorted(list(set(potential_telemarketers)))

print("These numbers could be telemarketers: ")
for m in potential_telemarketers:
    print(m)