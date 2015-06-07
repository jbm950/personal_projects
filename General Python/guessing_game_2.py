#-------------------------------------------------------------------------------
# Name:        guessing_game_2.py
# Purpose:     This game will have you think of a number between 1 and 500 and
#    the program will try to guess your number with input on whether its guesses
#    are too high or too low
#
# Author:      James
#
# Created:     15/06/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# Definiton of Variables
#    guess = this is pythons guess as to what your number is
#    low = this will hold the low end of the programs guessing range
#    high = this will hold the high end of the programs guessing range
#    n =  this is the number of guesses that the program makes to determine your
#         number
#    response = this is the input variable from the player saying whether the
#               guess is high, low or, correct

# Prepare the guessing range and import the necessary modules
import random
low = 0
high = 501
n = 1

# print to the screen how the game will work
print("Dear Contestant: This time the game is reversed!\n"
      "\t\tIt is my job to determine the number you are thinking of this time"
      " around.\n\t\t(The range from which you can pick your number is from 1 to 500"
      ")\n\t\tType ready when you have chosen your number.\n\n")

input()

while True:
    guess = random.randint(low+1,high-1)
    print('I guess that your number is %d. Is this guess high, low or'
          ' correct?' % guess)
    response = input()
    response.lower()
    if response == 'low':
        low = guess
    elif response == 'high':
        high = guess
    elif response == 'correct':
        print('Yay! I was able to determine your number! And it only took'
              ' %d tries!' % n)
        break
    else:
        print('Please enter low, high, or correct only')
        response = input()
    n += 1

