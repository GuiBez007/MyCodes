# Ask user to inform various numbers and keep them in a list even in its correct position, without use the
# sort functions. At the end, show them in ascending form.

print('Type below how many numbers you wish[S to stop]: ')
numbers = []

while True:
    number = input('> ').strip()

    if number in 'Ss':
        break

    if len(numbers) == 0:
        numbers.append(int(number))
        print(f'Number was added at the initial position \n')
    else:
        for i in range(len(numbers)):
            if int(number) < numbers[i]:
                numbers.insert(i, int(number))
                print(f'Number was added at position {i} \n')
                break
            elif i == len(numbers)-1:
                numbers.append(int(number))
                print(f'Number was added at the final position \n')
print(numbers)

input() #wait