# Write a code that the user can type any expression using parentheses. The program must analyze the expression
# and show user if it's valid or not according the opened and closed parentheses' quantity.

expression = input('Type your expression: ')
count = 0

for i in expression:
    if i == ')':
        count -= 1
    elif i == '(':
        count += 1
    if count < 0:
        break

if count == 0:
    print('Your expression is VALID!')
else:
    print('Your expression is INVALID!')

input() #wait