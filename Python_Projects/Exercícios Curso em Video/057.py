# Write a code that reads a person sex but just accept values M or F.
# Case wrong, ask the info again until the correct value has been inserted.


sex = ''
while sex != 'M' and sex != 'F':
    sex = input('Inform your sex[M/F]: ').strip().upper()
    if sex not in 'MF':
        print('Invalid info, try again!')

print('Alright, I got it!')

input() #wait