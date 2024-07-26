# Create a program where 4 players roll a die and get random results. Keep these values in a dictionary. At the end,
# put the dictionary in order showing the winner with the highest value.

from random import randint
from operator import itemgetter
game = {}

print('Inform the names of the 4 players')
for i in range(1, 5):
    player_name = input(f'- player {i}> ')
    number = randint(1, 6)
    game[player_name] = number

game = sorted(game.items(), key=itemgetter(1), reverse=True)

print(f'\n{game}')
for i in range(4):
    for x in range(2):
        if x == 0:
            print(game[i][x] + ':', end=' ')
        else: print(game[i][x])

input() #wait