#Write a code that reads four names and choice the order of them printing in the screen
from random import shuffle

name_1 = str(input('Type the first name: '))
name_2 = input('Now, the second: ')
name_3 = str(input('The third: '))
name_4 = input('And the fourth: ')
List = [name_1, name_2, name_3, name_4]

shuffle(List)
print('\nThe choiced person was {}'.format(List))

input() #wait
