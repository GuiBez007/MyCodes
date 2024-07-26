# Remake the 9º challenge showing the multiplication table of a number -chosen- by user, using the loop for

table = int(input('Inform what multiplication table do you wanna see: '))
for i in range(10):
    print('{:2} * {} = {}'.format(i+1, table, (i+1) * table))

input() #wait