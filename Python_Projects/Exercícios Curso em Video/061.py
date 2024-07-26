# Remake the challenge 51 reading the first term and the PA reason, showing the first 10 PA terms using the loop while.

first_term = int(input('Type the first PA term: '))
reason = int(input('Now inform the PA reason: '))

i = 1
while i <= 10:

    if i == 10:
        print(first_term)
    else:
        print('{}'.format(first_term), end=' -> ')
        first_term += reason
    i += 1

input() #wait