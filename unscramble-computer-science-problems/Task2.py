"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
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

dials = {call[0]: int(call[3]) for call in calls}
receives = {call[1]: int(call[3]) for call in calls}
receives_ex_dials = dict()

for (k, v), (k2, v2) in zip(dials.items(), receives.items()):
    if k in receives.keys():
        dials[k] = v + receives[k]
    if k2 not in dials.keys():
        receives_ex_dials[k2] = v2

dials.update(receives_ex_dials)

max_phone = max(dials, key=lambda key: dials[key])

print(f"{max_phone} spent the longest time, {dials[max_phone]} seconds, on the "
      f"phone during September 2016.")