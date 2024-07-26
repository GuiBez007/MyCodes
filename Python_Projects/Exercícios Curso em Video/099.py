# Write a program that has a function named higher(), that receives integer parameters.
# Your program must analyze the values and show which one is the highest value.

def higher(num):
    highest = 0
    for i in range(len(num)):
        if i == 0:
            highest = num[0]
        elif num[i] > highest:
            highest = num[i]
    print(f'The highest number is {highest}!')


# main()
numbers = []
print('Type below how many numbers you want [S to STOP]')
while True:
    aux = input('> ')
    if aux[0] in 'Ss':
        break
    numbers.append(int(aux))
higher(numbers)

input() #wait