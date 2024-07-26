# Remake the challenge 28 where the CPU 'think' a number in range 0 - 10, but now the player will try to
# choose the correct number, showing at the end how many tries was necessary until the player wins.

from random import randint

cpu_number = randint(0, 10)
player_number = 0
tries = 0

print('You\'re stuck in a 1-10 loop! \n')
while player_number != cpu_number:
    tries += 1
    player_number = int(input('What\'s the correct number chose by me? \nTry {}: '.format(tries)))

    if player_number != cpu_number:
        print('Haha wrong answer, try again! \n')

print('Ok, ok. You win this time! \nYou\'ve needed {} tries to guess the right number!'.format(tries))

input() #wait