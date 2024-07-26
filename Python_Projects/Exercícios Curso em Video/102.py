# Create a program that has a function named factorial() that receives two parameters: the first one indicates the
# number will be calculated, and the other named show that will be a logic value (optional) indicating if the
# calculating process will be showed or not in the screen.

def factorial(number, show=False):
    results = []
    aux = number
    for i in range(number, 1, -1):
        aux = aux * (i-1)
        results.append(aux)

    if show == True:
        print(f'{number} * {number-1} = {results[0]}')
        number -= 1
        for i in range(len(results)-1):
            print(f'{results[i]} * {number-1} = {results[i+1]}')
            number -= 1
    return results[-1]


# main()
number = int(input('Type a number to calculate its factorial> '))
answer = input('Do you wish to see the calculate process?[Y/N]> ').strip().upper()[0]
if answer == 'Y': answer = True
else: answer = False
print(f'The factorial of {number} is {factorial(number, answer)}')

input() # wait