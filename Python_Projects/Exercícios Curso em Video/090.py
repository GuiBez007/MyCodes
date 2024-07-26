# Write a program that reads the name and average of a student and keep these information in a dictionary.
# At the end, show the all dictionary content.

dictionary = {}
print('Inform your name and average below')

name = input('name> ')
average = float(input('average> '))

dictionary = {'name': name, 'average': average}

print(f'\n- name is {name} \n- average is {average}')
if dictionary['average'] < 5:
    print('- situation is\033[31m REPROVED!')
elif dictionary['average'] < 7:
    print('- situation is\033[34m RECOVERY!')
else:
    print('- situation is\033[32m APPROVED!')

input() #wait