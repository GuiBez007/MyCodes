# Write a code that reads the born year of an athlete and show his category according his age:
# till 9 years MIRIM / till 14 CHILD / till 19 JUNIOR / till 25 SENIOR

from datetime import date

age = (int(input('Inform your born year: ')) - date.today().year) * -1

print('Your age is {} so your category is '.format(age), end='')
if age <= 9:
    print('MIRIM!')
elif age <= 14:
    print('CHILD!')
elif age <= 19:
    print('JUNIOR!')
elif age <= 25:
    print('SENIOR!')
else:
    print('You not exist!')

input() #wait