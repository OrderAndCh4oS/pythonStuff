#!/usr/bin/python3

num = int(input("Enter a number to convert to binary: "))

if num < 0:
    num = abs(num)
    isNegative = True
else:
    isNegative = False

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

if isNegative:
    result = '-' + result

print(result)
