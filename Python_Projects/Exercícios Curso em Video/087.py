# Upgrade the last challenge showing at the end:
# - the sum of all even values
# - the sum of third column values
# - the highest value of second line

matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
_sum = 0

print('Inform the numbers that will be placed in the matriz: ')
for n in range(2):
    for i in range(3):
        for x in range(3):
            if n == 0:
                matriz[i][x] = int(input('[{},{}]> '.format(i, x)))
                if matriz[i][x] % 2 == 0:
                    _sum += matriz[i][x]
            else:
                print(f'[{matriz[i][x]:5}]', end='')
                if x == 2:
                    print()

print(f'The sum of all even values is {_sum}')
print(f'The sum of the third column values is {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'The second line highest value is {max(matriz[1])}')

input() #wait