# Rewrite the function readInt() we did in challenge 104, now including the possibility of typing a wrong type
# number. Create a function called readFloat() too with the same functionality.

def readInt(message, type=int):
    return validation(message, type)


def readFloat(message, type=float):
    return validation(message, type)


def validation(message, type):
    while True:
        try:
            number = type(input(message))
        except (ValueError, TypeError):
            print('\033[31mInvalid informed value! \033[m \n')
        except KeyboardInterrupt:
            print('\033[33m \nThe user have decided to stop the program execution! \033[m \n')
            exit()
        else:
            return number


# main()
number_1 = readInt('Type a int number> ', int)
number_2 = readFloat('Type a float number> ', float)
print(f'\033[32mYour int number is {number_1}! \033[m')
print(f'\033[32mYour float number is {number_2}! \033[m')

input() #wait