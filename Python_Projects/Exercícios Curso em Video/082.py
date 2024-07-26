# Create a loop to put numbers in a list and more two lists to organize the odd number in one of them and
# the pair number in the other. At the end, show the three lists.

numbers = []
odd = []
even = []

print('Type below how many numbers you wish[S to stop]: ')
while True:
    number = input('> ').strip()
    if number in 'Ss':
        break
    numbers.append(int(number))

    if int(number) % 2 == 0:
        even.append(int(number))
    else:
        odd.append(int(number))

print(numbers)
print(f'The odd numbers are {odd}')
print(f'The even numbers are {even}')

input() #wait