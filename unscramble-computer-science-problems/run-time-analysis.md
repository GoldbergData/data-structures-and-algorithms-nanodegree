Runtime Analysis for Unscramble Computer Science Problems
================
Joshua Goldberg
May, 12 2019

The below runtime analyses are Worst Case Big-O approximations.

# Task 0

What is the first record of texts and what is the last record of
calls?

``` python
print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time "
      f"{texts[0][2]}.")

print(f"First record of calls, {calls[0][0]} calls {calls[0][1]} at time "
      f"{calls[0][2]}, lasting {calls[0][3]} seconds.")
```

Notation: \(O(1)\). The operations are not dependent on iteration.

# Task 1

How many different telephone numbers are there in the records?

``` python
numbers = set()

for text, call in zip(texts, calls):
    for i in range(0, 2):
        numbers.add(text[i])
        numbers.add(call[i])

print(f"There are {len(numbers)} different telephone numbers in the records.")
```

Notation: \(O(n)\). Though we have two explicit `for` loops, the inner
loop is just a short-hand for extended code. In other words, it does not
depend on the input (\(n\)).

# Task 2

Which telephone number spent the longest time on the phone during the
period? Don’t forget that time spent answering a call is also time spent
on the phone.

``` python
max_duration = max([int(call[3]) for call in calls])

max_call = calls[[call[3] for call in calls].index(str(max_duration))]

print(f"{max_call[0]} spent the longest time, {max_duration} seconds, "
      f"on the phone on {max_call[2]}.")
```

Notation: \(O(n^5)\). `max()`, two explicit `for` loops, and indexing
through look to find
    match.

  - [how-efficient-is-pythons-max-function](https://stackoverflow.com/questions/5454030/how-efficient-is-pythons-max-function)

  - [complexity-of-list-index-in-python](https://stackoverflow.com/questions/5913671/complexity-of-list-indexx-in-python).

# Task 3

The area code for fixed line telephones in Bangalore is “(080)”. Fixed
line numbers include parentheses, so Bangalore numbers have the form
(080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. - Fixed lines start with an area code enclosed in
brackets. The area codes vary in length but always begin with 0. -
Mobile numbers have no parentheses, but have a space in the middle of
the number to help readability. The prefix of a mobile number is its
first four digits, and they always start with 7, 8 or 9. -
Telemarketers’ numbers have no parentheses or space, but they start
with the area code 140.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with “(080)”, what percentage of these calls were
made to a number also starting with
“(080)”?

``` python
bangalore_calls = [call for call in calls if call[0].startswith("(080)")]

bangalore_dialed = [call[1] for call in bangalore_calls]

called_areas = []

for call in bangalore_dialed:
    if re.search("\(\w+\)", call):
        called_areas.append(re.search(r'(\(.*?\))', call).group(1))
    elif re.search(r'(^[7|8|9])', call):
        called_areas.append(call[0:4])
    clean_calls = sorted(list(set(called_areas)))
    print("The numbers called by people in Bangalore have codes:")
    for call in clean_calls:
        print(call)

total_calls = len(bangalore_calls)

bangalore_to_bangalore = len([call for call in bangalore_calls if call[
    1].startswith("(080)")])

percentage = round(bangalore_to_bangalore / total_calls, 4) * 100

print(f"{percentage} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
```

Notation: \(O(n^2 + nlog_n)\). We have two explicit `for` loops. Regex
is typically \(O(n)\)
([what-is-the-complexity-of-regular-expression](https://stackoverflow.com/questions/4378455/what-is-the-complexity-of-regular-expression)),
but we are checking with an `if` statement, so no sequencing is needed.
`sorted()` introduces \(O(nlog_n)\), according to python
[documentation](https://wiki.python.org/moin/TimeComplexity).

# Task 4

The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: these are
numbers that make outgoing calls but never send texts, receive texts or
receive incoming calls.

``` python
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
```

Notation: \(n^6+nlog_n\). Five explicit `for` loops, `sorted()`, and
operation on `zip` object results in \(O(n)\)
([what-is-the-time-complexity-of-zip-in-python](https://stackoverflow.com/questions/36877715/what-is-the-time-complexity-of-zip-in-python)).
