# Write a code that permit play 'Jokenpô' against the CPU
# OBS> without loops version (not complete game)

from random import randint
from os import system

# computer moves
computer_rock = '      ._____.      \n'\
                '     (____)  \\____\n'\
                '     (_____)       \n'\
                '     (_____)       \n'\
                '     (____)        \n'\
                '      (___)__.----   '

computer_paper = '   ._________.     \n'\
                 '  (________   \\___\n'\
                 '(______            \n'\
                 '(_______           \n'\
                 '  (_______         \n'\
                 '   (__________.---   '

computer_scisor = '       ._____.     \n'\
                  '      (____   \\___\n'\
                  ' (______           \n'\
                  '(__________        \n'\
                  '      (____)       \n'\
                  '       (___)__.---   '


# GAME
n = 10  #quantity of spaces between the hands
print('===== JOKENPO GAME ===== \n'
      '| [01] - Rook;         | \n'
      '| [02] - Paper;        | \n'
      '| [03] - Scisor.       | \n'
      '========================   ')
player = int(input('Make your game: '))
computer = randint(1, 3)

if player not in [1,2,3]:
    print('Invalid option! Game over!')
else:
    print('PLAYER game> ', end='')
    # player hand
    if player == 1:
        print('ROCK', end='\n')
    elif player == 2:
        print('PAPER', end='\n')
    elif player == 3:
        print('SCISOR', end='\n')

    print('CPU game: ')
    # computer hand
    if computer == 1:
        print(computer_rock, end='')
    elif computer == 2:
        print(computer_paper, end='')
    elif computer == 3:
        print(computer_scisor, end='')

    print()
    #gamerulers
    if player == computer:
        print('Draw!')
    elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        print('Player wins!')
    elif computer == 1 and player == 3 or computer == 2 and player == 1 or computer == 3 and player == 2:
        print('CPU wins!')

input() #wait
