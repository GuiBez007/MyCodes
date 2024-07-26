# Upgrade the last challenge asking user if he wants to show more terms. The program ends when user types 0 to not see more terms.

term = int(input('Type the first PA term: '))
reason = int(input('Now inform the PA reason: '))
terms_count = 0

i = 1
while i != 0:
    i = int(input('\nHow many terms do you wanna see [0=STOP]: '))

    if i == 0:
        print('The total terms showed was {}.'.format(terms_count))
    elif i > 0:
        while i != 0:
            terms_count += 1
            print('{}'.format(term), end=' -> ')
            term += reason
            i -= 1
        i += 1
    else:
        print('Invalid value!')

input() #wait