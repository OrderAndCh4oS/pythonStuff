#!/usr/bin/python3
y = int(input("Enter a number to find square root: "))
epsilon = 0.01
guess = y / 2
while abs(guess*guess - y) >= epsilon:
    guess = guess - ((guess**2 - y)/(2*guess))
print(str(guess))
