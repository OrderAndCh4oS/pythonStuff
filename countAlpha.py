#!/usr/bin/python3
s = "bqltookjirgaiicezvtwwie"
string = ''
longest = ''
currentChar = 'a'
alpha = "abcdefghijklmnopqrstuvwxyz"
for c in s:
    if ord(c) >= ord(currentChar):
        string += c
    else:
        string = c
    if len(string) > len(longest):
        longest = string
    currentChar = c
print("Longest substring in alphabetical order is: " + str(longest))
