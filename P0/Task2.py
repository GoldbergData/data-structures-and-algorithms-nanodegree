"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('P0/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone 
during September 2016.".
"""

max_duration = max([int(call[3]) for call in calls])

max_call = calls[[call[3] for call in calls].index(str(max_duration))]

print(f"{max_call[0]} spent the longest time, {max_duration} seconds, "
      f"on the phone on {max_call[2]}.")

"""
Calculate Big O
max: https://stackoverflow.com/questions/5454030/how-efficient-is-pythons-max-function
O(n + 2) n for max; 2 for subset and print
"""