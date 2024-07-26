# Write a code that can read two numbers and compare them, printing in the screen a message:
# The first is bigger, the second is bigger or the both are the same

number_1 = int(input('Type the first number: '))
number_2 = int(input('Type the second number: '))

if number_1 > number_2:
    print('The first number ({}) is the bigger!'.format(number_1))
elif number_2 > number_1:
    print('The second number ({}) is the bigger!'.format(number_2))
else:
    print('Both numbers are the same!')

input() #wait