# Write a code that reads an integer number and show if he's a prime number or not.

count = 0
first_primes = [2, 3, 5, 7]
number = (int(input('Type a integer number: ')))

if number < 2:
    print('The informed number IS NOT a prime number!')
else:
    for i in range(2, 10):
        if number % i == 0:
            count += 1

    if count == 0 or number in first_primes:
        print('The informed number IS a prime number!')
    else:
        print('The informed number IS NOT a prime number!' )

input() #wait