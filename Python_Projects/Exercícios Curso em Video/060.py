# Write a code that reads a number and shows its factorial
# EX> 5! = 5 x 4 x 3 x 2 x 1 = 120

number = int(input('Type the number that will have its factorial calculated: '))

i = number
old_number = i
_sum = 0

while i != 1:
    print('{} * {} = {}'.format(number, i-1, number*(i-1)))
    number *= i-1
    i -= 1
print('-> {}! is equal {} <-'.format(old_number, number))

input() #wait