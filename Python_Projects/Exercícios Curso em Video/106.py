# Make a micro-system that utilizes the Interactive Python Help. The user will type the command and the manual will
# appear. When user types word 'END', the program will end. Important: use colors.

def c(back):
    """
    0 = black / 1 = red / 2 = green / 3 = yellow / 4 = blue / 5 = purple / 6 = cian / 7 = gray 
    """""
    color = 0
    return f'\033[0;3{color};4{back}m'


def HELP(command):
    print(f'{c(r(1, 6))}')
    help(command)
    print(f'{c(7)}')


# main()
from random import randint as r
while True:
    command = input('See more about function> ').strip()
    if command.upper() == 'END':
        print('The program has stopped!')
        break
    HELP(command)

input() #wait