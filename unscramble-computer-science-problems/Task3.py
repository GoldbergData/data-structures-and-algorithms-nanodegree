"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

bangalore_calls = [call for call in calls if call[0].startswith("(080)")]

bangalore_dialed = [call[1] for call in bangalore_calls]

called_areas = []

for call in bangalore_dialed:
    if re.search("\(\w+\)", call):
        called_areas.append(re.search(r'(\(.*?\))', call).group(1))
    elif re.search(r'(^[7|8|9])', call):
        called_areas.append(call[0:4])
    clean_calls = sorted(list(set(called_areas)))

print(f"The numbers called by people in Bangalore have codes: {clean_calls}")

total_calls = len(bangalore_calls)

bangalore_to_bangalore = len([call for call in bangalore_calls if call[
    1].startswith("(080)")])

percentage = round(bangalore_to_bangalore / total_calls, 4) * 100

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls "
      f"to other fixed lines in Bangalore.")
