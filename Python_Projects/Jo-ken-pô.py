# Write a code that permit play 'Jokenpô' against the CPU

from random import randint
from time import sleep
from os import system

# player moves
player_rock = ['     ._____.       ',
               '____/  (____)      ',
               '      (_____)      ',
               '      (_____)      ',
               '       (____)      ',
               '----.__(___)       ']

player_paper = ['    .__________.   ',
                '___/    ________)  ',
                '           ______) ',
                '          _______) ',
                '         _______)  ',
                '---.__________)    ']

player_scisor = ['    ._____.       ',
                 '___/   ____)      ',
                 '          ______) ',
                 '       __________)',
                 '      (____)      ',
                 '---.__(___)       ']


# computer moves
computer_rock = ['      ._____.      ',
                 '     (____)  \\____',
                 '     (_____)       ',
                 '     (_____)       ',
                 '     (____)        ',
                 '      (___)__.---- ']

computer_paper = ['   ._________.     ',
                  '  (________   \\___',
                  '(______            ',
                  '(_______           ',
                  '  (_______         ',
                  '   (__________.--- ']

computer_scisor = ['       ._____.     ',
                   '      (____   \\___',
                   ' (______           ',
                   '(__________        ',
                   '      (____)       ',
                   '       (___)__.--- ']


# GAME
player_points = computer_points = 0
n = 10 # quantity of spaces between the hands
while True:
    print('===== JOKENPO GAME ===== \n'
          '| [01] - Rook;         | \n'
          '| [02] - Paper;        | \n'
          '| [03] - Scisor.       | \n'
          '========================   ')
    print('SCORE -> player: {} / cpu: {}'.format(player_points, computer_points))
    player = input('Make your game: ')
    computer = randint(1, 3)

    if player not in ['1','2','3']:
        system('cls')
        print('Invalid option!')
        continue

    print()
    for i in range(6):
        # player hand
        if player == '1':
            print(player_rock[i], end=' ' *n)
        elif player == '2':
            print(player_paper[i], end=' ' * n)
        elif player == '3':
            print(player_scisor[i], end=' ' * n)

        # computer hand
        if computer == 1:
            print(computer_rock[i])
        elif computer == 2:
            print(computer_paper[i])
        elif computer == 3:
            print(computer_scisor[i])

    print()
    player = int(player)
    
    #gamerulers
    if player == computer:
        print('Draw!')
    elif player == 1 and computer == 3 or player == 2 and computer == 1 or player == 3 and computer == 2:
        player_points += 1
        print('Player +1 point!')
    elif computer == 1 and player == 3 or computer == 2 and player == 1 or computer == 3 and player == 2:
        computer_points += 1
        print('CPU +1 point!')


    sleep(3)
    # points of players (P1+CPU)
    if player_points == 3:
        print('Player wins!!!')
        break
    elif computer_points == 3:
        print('CPU wins!!!')
        break
    else:
        system('cls')

input() #wait
