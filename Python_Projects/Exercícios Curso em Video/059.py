# Write a program that reads two values and shows a menu of options:
# sum / multiply / higher / new numbers / exit program

print('Type two values to continue')
number_1 = float(input('Number 1: '))
number_2 = float(input('Number 2: '))
print('')

option = 1
while option != 0:
    print('=-'*18             +'\n'
          '[01] - Sum;          \n'
          '[02] - Multiply;     \n'
          '[03] - Higher value; \n'
          '[04] - New values;   \n'
          '[05] - Exit program.   ')
    option = int(input('Choose an option: '))

    if option == 1:
        print('The sum of {:.2f} and {:.2f} is {:.2f}'.format(number_1, number_2, number_1+number_2))
    elif option == 2:
        print('The multiplication of {:.2f} and {:.2f} is {:.2f}'.format(number_1, number_2, number_1 * number_2))
    elif option == 3:
        print('The higher value is ', end='')
        if number_1 > number_2:
            print('{}'.format(number_1), end='\n')
        else:
            print('{}'.format(number_2), end='\n')
    elif option == 4:
        print('Inform the new values')
        number_1 = float(input('Number 1: '))
        number_2 = float(input('Number 2: '))
    elif option == 5:
        option = 0
    else:
        print('Invalid option!')

print('Exit with success! Until the next time! \n' + '=-' *18)

input() #wait
