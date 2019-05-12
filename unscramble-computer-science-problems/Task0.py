"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('unscramble-computer-science-problems/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('unscramble-computer-science-problems/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time "
      f"{texts[0][2]}.")

print(f"First record of calls, {calls[0][0]} calls {calls[0][1]} at time "
      f"{calls[0][2]}, lasting {calls[0][3]} seconds.")

"""
Calculate Big O
O(2) since we run two print statements irrespective of input.
"""