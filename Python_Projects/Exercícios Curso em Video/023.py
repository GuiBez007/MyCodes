#Write a code that reads a number of 0 to 9999 and print its units, tens, hundreds and thousands

number = int(input('Type a integer number here: '))
#print('{} units \n{} tens \n{} hundreds \n{} thousands'.format(number[3], number[2], number[1], number[0])) WRONG!
print('{} units \n{} tens \n{} hundreds \n{} thousands'.format(number // 1 % 10, number // 10 % 10,\
    number // 100 % 10, number // 1000 % 10))

input() #wait