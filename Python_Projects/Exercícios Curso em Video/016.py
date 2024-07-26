#Write a code that can reads a real number and print his integer part
from math import trunc

float_number = float(input('Type a real number: '))
print('The integer part of the previous number is {}.'.format(trunc(float_number)))

input() #wait
