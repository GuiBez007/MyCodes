# Write a code that has a random number(0 to 5) and ask for the user to find out what number is that

import random

random_number = random.randint(0, 5)
user_number = int(input('Type the correct number that you think be: '))
if user_number == random_number:
    print('You\'ve won this time!')
else:
    print('You lose! The correct number was {}'.format(random_number))

input() #wait