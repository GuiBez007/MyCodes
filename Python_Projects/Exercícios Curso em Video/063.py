# Write a code that reads a natural number and shows the first N Fibonacci sequence elements:
# EX> 0 – 1 – 1 – 2 – 3 – 5 – 8

elements = int(input('How many terms to show?: '))

term_1 = count = 0
term_2 = aux = 1

while count != elements:
    if count == elements - 1:
        print('{}'.format(term_1))
    else:
        print('{}'.format(term_1), end='|')

    count += 1
    aux = term_2
    term_2 += term_1
    term_1 = aux

input() #wait