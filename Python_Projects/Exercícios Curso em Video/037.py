# Write a code that can read an integer number and ask user to choice what will be the conversion base:
# 1 to binary / 2 to octal / 3 to hexadecimal

print('===== BASE CONVERSION =====')
number = int(input('Type a number in decimal: '))
print('[01] - to binary;')
print('[02] - to octal;')
print('[03] - to hexadecimal.')
base = int(input('Type the base you wish to convert: '))

if base == 1:
    print('The number {} in binary is {}'.format(number, bin(number)[2:]))
elif base == 2:
    print('The number {} in octal is {}'.format(number, oct(number)[2:]))
elif base == 3:
    print('The number {} in hexadecimal is {}'.format(number, hex(number)[2:]))
else:
    print('Invalid option!')

input() #wait