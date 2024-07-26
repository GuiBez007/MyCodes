# Get 5 values and put them in a list. At the end, show what was the highest, what was the lowest and them positions.

numbers = []
positions = ('first', 'second', 'third', 'fourth', 'fifth')
highest = lowest = hi = li = 0

print('Type 5 values below to see some information!')
for i in range(5):
    numbers.append(int(input(f'Inform the {positions[i]} value: ')))
    if i == 0:
        highest = lowest = numbers[0]
    else:
        if numbers[i] > highest:
            highest = numbers[i]
            hi = i
        if numbers[i] < lowest:
            lowest = numbers[i]
            li = i

print(f'\nYou typed the values {numbers} where the \n'
      f'HIGHEST number was {highest} in {positions[hi]} position \n'
      f'and the LOWEST number was {lowest} in {positions[li]} position.')

input() #wait