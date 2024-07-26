# Write a program that reads the born year of seven people. At the end, show how many people didn't reach 18 years old
# yet and how many even are adults

from datetime import date

years = [0] * 7
adults = 0
not_adults = 0

for i in range(7):
    years[i] = int(input('{}# Type your born age: '.format(i+1)))
    years[i] = date.today().year - years[i]

    if years[i] >= 18:
        adults += 1
    else:
        not_adults += 1

print('There are {} adult people and {} who don\'t are adult'.format(adults, not_adults))

input() #wait
