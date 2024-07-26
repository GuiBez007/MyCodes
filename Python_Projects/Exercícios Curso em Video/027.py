# Write a code that can reads a full person's name and print just his first and his last name

full_name = input('Type your full name here: ')
print('Your first name is {} and your last is {}'.format((full_name.split()[0].upper()),\
    (full_name.split()[len(full_name.split())-1].upper())))

input() #wait