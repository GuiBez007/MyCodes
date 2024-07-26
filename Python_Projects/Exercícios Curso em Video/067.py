# Write a code that shows the multiplication table, one by one, for each typed value by user.
# The program will be stopped when the number is negative.

print('Enter numbers to see its multiplication table: ')
while True:
    number = int(input('> '))
    if number < 0:
        break

    print('=== TABLE OF {} ==='.format(number))
    for i in range(10):
        print(' {} * {} = {}'.format(i+1, number, (i+1) * number))
    print('================')

print('Program has been stopped!')
input() #wait