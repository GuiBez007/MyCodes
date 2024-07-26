# Write a code that plays odd or even with CPU. The game just be stopped when player loses,
# showing the total of consecutive victories that he has conquered at the end of game.

from random import randint

wins = 0
while True:
    print('===== ODD/EVEN GAME =====')

    player = int(input('Type a number: '))
    computer = randint(0, 11)
    total = player + computer

    print('   [01] - odd;            \n'
          '   [02] - even.           \n'
          '=========================   ')
    option = int(input('> '))

    if total % 2 == 0 and option == 2 or total % 2 == 1 and option == 1:
        print('Player +1 point! \n')
        wins += 1
    else:
        print('CPU wins! \nThe player have marked {} points!'.format(wins))
        break

input() #wait