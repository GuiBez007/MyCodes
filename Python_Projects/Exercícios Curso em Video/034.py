# Write a code that informs the new salary of the worker

salary = float(input('Type your salary here: '))
if salary > 1250:
    print('Your new salary is {:.2f}'.format(salary + (salary / 100) * 10))
else: print('Your new salary is {:.2f}'.format(salary + (salary / 100) * 15))

input() #wait