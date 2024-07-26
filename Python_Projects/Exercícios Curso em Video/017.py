#Write a program that reads the values of "catetos" and calculates the hypotenuse
from math import pow #, hypt

cateto_adjacente = float(input('Type the cateto\'s value: '))
cateto_oposto = float(input('Now the other value: '))

hypotenuse = (pow(cateto_adjacente, 2) + pow(cateto_oposto, 2)) ** 0.5 #or = math.hypt(cateto_1, cateto_2)
print('The hypotenuse is {:.2f}'.format(hypotenuse))

input() #wait
