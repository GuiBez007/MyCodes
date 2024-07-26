# Write a code that helps the MEGA SENA's player to create guesses. The program will ask how many games will be
# done and draw 6 numbers in range 1-60 for each game, registering all in a compost list.

guesses = []
aux = []
from random import randint as rand
from time import sleep

games_quantity = int(input('Games\' quantity: '))
for game in range(games_quantity):
    for number in range(6):
        aux.append(rand(1, 60))

    guesses.append(aux[:])
    aux.clear()

print('\n=-=-=-=-=- Your guesses -=-=-=-=-=')
for i in range(games_quantity):
    print(f'{i+1}°game> {guesses[i]}')
    sleep(1)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

input() #wait