# Write a code that calculates the sum between all numbers which are multiples
# of three and are within the range of 1 - 500

_sum = 0
count = 0

for i in range(3, 501, 3):
    _sum += i
    count += 1
print('The sum of all the {} first numbers until 500 multiples of three is {}.'.format(count, _sum))

input() #wait
