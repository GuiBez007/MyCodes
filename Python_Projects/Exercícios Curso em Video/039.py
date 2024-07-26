# Write a code that reads someone's born year and inform if he still needs to enlist,
# if it's time to enlist or if even passed the time
# The program must show the remaining time to enlist or the time already passed

from datetime import date

born_year = int(input('Inform your born year: '))
actual_year = date.today().year

print('Who has born in {} have {} in {} \n'.format(born_year, actual_year-born_year, actual_year))
if (actual_year - born_year) < 17:
    print('You\'ve escaped for now, you are free! \nYour enlist year is {}'.format(actual_year + (17 - (actual_year - born_year))))
elif (actual_year - born_year) > 17:
    print('You\'re late! Your enlist year was {}'.format(actual_year - ((actual_year - born_year) - 17)))
else:
    print('You\'re in time! Go to enlist now!')

input() #wait