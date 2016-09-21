#!/usr/bin/python3

aStr = "abcdefghij"
char = "b"

def findChar(char, aStr):
    if len(aStr) % 2 == 0 and len(aStr) != 1:
        mid = int(len(aStr)/2)
    elif len(aStr) == 1:
        mid = 0
    else:
        mid = int(len(aStr)/2)+1
    print(mid)
    print(aStr)
    if aStr[mid] == char:
        return True
    elif mid == 0:
        return False
    elif ord(aStr[mid]) > ord(char):
        return findChar(char, aStr[:mid])
    else:
        return findChar(char, aStr[-mid:])

found = findChar(char, aStr)
print(found)
