#-------------------------------------------------------------------------------
# Name:        Guessing game.py
# Purpose: This module will be a text based numeric guessing game. The player
#   will get 10 guesses to guess a number between 1 and 100. After each guess
#   the system will let the player know if their guess was too high or too low.
#
# Author:      James
#
# Created:     13/01/2014
# Copyright:   (c) James 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
#
# Definiton of Varibles:
#  guess = this will be the guess by the player
#  n = this is the number of guess the player gets to make
#  correct = this is the integer that will be created at random from 1 to 100
#      that the player has to guess
#  win = this will turn to a 1 if the player correctly guesses the number in
#      order to let the system know that the win condition has been met.

# Import the random module so that a random integer can be created which the
# player has to guess.

import random

# Initialize the guess count and create the random number that the player will
# have to guess. Also set the win condition to 0.

n = 0
correct = random.randint(1,100)
win = 0

# Print to the screen the rules of the game.
print('''Dear contestant,
You will have a total of 10 guesses to determine the magic number.
                                                        Good luck!
                           (Hint the number lies between 1 and 100)''' )

# Start the while loop that will run the game. The loop will start by asking
# for input from the player and then compare that value to the randomly created
# value. If the value is not the randomly created value the system will let the
# player know if the guess was high or low. If the number of guesses reaches 10
# the loop will exit and the player will have lost.

while True:
    guess = int(input('What is your guess as to the magic number?'))
    if guess == correct:
        win = 1
        break
    elif n == 10:
        break
    elif guess > correct:
        print('Your guess of %d was too high' % guess)
    elif guess < correct:
        print('Your guess of %d was too low' % guess)
    n = n + 1

# Now check the win condition. If it has been met display the congratulations
# and if now display the loss message.

if win == 1:
    print('Congratulations you guessed the magic number %d' % correct)
elif win == 0:
    print("I'm sorry you have ran out of guesses. The magic number was %d" % correct)










