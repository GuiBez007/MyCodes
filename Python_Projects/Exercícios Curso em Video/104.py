# Write a program that has a function called readInt(), that will work as the Python function input(), but doing
# the check to accept just a numeric value. EX: n = readInt('Type a n: ')

def readInt(message):
    while True:
        number = input(message)
        if number.isnumeric():
            return int(number)
        print('\033[31mNot valid! \033[m \n')


# main()
number = readInt('Type a number> ')
print(f'\033[32mYour number is {number}! \033[m')

input() #wait