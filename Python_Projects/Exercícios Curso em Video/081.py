# Create a loop to get numbers and then show:
# - How many numbers was typed
# - The list of values in descending form
# - If the value 5 was typed and is in or not in list

numbers = []
print('Type below how many numbers you wish[S to stop]: ')
while True:
    number = input('> ').strip()
    if number in 'Ss':
        break
    numbers.append(int(number))

print(f'\n{sorted(numbers)[::-1]}')
print(f'Total elements is {len(numbers)};')
print(f'The number 5 is in the list = {5 in numbers}.')

input() #wait