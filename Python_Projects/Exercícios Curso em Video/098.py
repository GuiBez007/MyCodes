# Write a program that has a function named count(), that receive 3 parameters: begin, end and pass.
# Your program has to realize 3 counts by the created function:
# - in range 1-10, 1 by 1
# - in range 10-0, 2 by 2
# - a personalized count

def count(begin, end, _pass):
    for i in range(begin, end, _pass):
        print(i, end=' ')
    print()


# main()
print('in range 1-10, 1 by 1')
count(1, 11, 1)

print('\nin range 10-0, 2 by 2')
count(10, -1, -2)

print('\nNow it\'s your time')
begin = int(input('BEGIN> '))
end = int(input('END> '))
_pass = int(input('PASS> '))

print('\nin range {}-{}, {} by {}'.format(begin, end, _pass, _pass))
count(begin, end, _pass)

input() #wait