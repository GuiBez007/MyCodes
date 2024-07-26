# Create a menu in Python using module.

from time import sleep
import usefulCeV.ex115.archive as archive
n = 45

def c(color=9):
    return f'\033[3{color}m'


def mold(message):
    line()
    print(f'{message:^{n}}')
    line()


def line():
    print('-' * n)


def options():
    print('{}1 - {}To see registered people;'.format(c(3), c(4)))
    print('{}2 - {}To register someone;'.format(c(3), c(4)))
    print('{}3 - {}To leave the system.{}'.format(c(3), c(4), c()))
    line()


def verification():
    while True:
        try:
            option = int(input('{}Your choice> {}'.format(c(2), c())))
        except (ValueError, TypeError):
            print('{}Invalid option, try again!{}'.format(c(1), c()))
        except KeyboardInterrupt:
            print('\nThe user doesn\'t want to continue!')
            print('Closing the system!')
            sleep(1)
            exit()
        else:
            if option == 1:
                archive.readFile('registeredPeople.txt')
                sleep(2)
            elif option == 2:
                archive.writeFile('registeredPeople.txt')
                sleep(2)
            elif option == 3:
                mold('Closing the system!')
                sleep(1)
                exit()
            else:
                print('{}Invalid option, try again!{}'.format(c(1), c()))
                continue
            break
