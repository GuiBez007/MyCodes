# write a code that reads the first term and the reason of a PA. At the end, show
# the 10 first terms of that progression.

print('{}\n Arithmetic Progression \n{}'.format('='*25, '='*25))

first_term = int(input('Type the first term of the PA: '))
reason = int(input('Now, the reason of the PA: '))

for i in range(10):
      if i != 9:
            print('{}'.format(first_term), end=' -> ')
            first_term += reason
      else:
            print('{}'.format(first_term))

input() #wait
