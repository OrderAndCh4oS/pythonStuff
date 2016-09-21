#!/usr/bin/python3
s = "bobbdbobbbobboobubobbbboebobcobobobobob"
count = 0
tracker = 0
test = ['b', 'o', 'b']
for char in s:
    if char == test[tracker]:
        tracker += 1
    elif char == test[0]:
        tracker = 1
    else:
        tracker = 0
    if tracker == 3:
        tracker = 1
        count += 1
print('Number of times bob occurs is: ' + str(count))
