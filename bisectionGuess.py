#!/usr/bin/python3

high = 100
low = 0
indicator = ''

print("Please think of a number between 0 and 100!")
while indicator != 'c':
    mid = int((high + low) / 2)
    print("Is your secret number ", mid, "?")
    indicator = input("Indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if indicator not in ['c', 'l', 'h']:
        print("Sorry, I did not understand your input.")
    elif indicator == 'l':
        low = mid
    elif indicator == 'h':
        high = mid
    else:
        print("Game over. Your secret number was: ", mid)
