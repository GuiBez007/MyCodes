# Write a program that informs the user if a year is leap or not
from datetime import date

year = int(input('Type the year here or 0 to actual year: '))
if year == 0:
    year = date.today().year
if year % 4 == 0:
    print('This is a leap year')
else: print('This is NOT a leap year')

input() #wait