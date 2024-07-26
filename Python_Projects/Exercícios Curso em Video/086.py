# Declare a matriz 3x3 and fill it with values. At the end, show the matriz with the correct format.

matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]

print('Inform the numbers that will be placed in the matriz: ')
for n in range(2):
    for i in range(3):
        for x in range(3):
            if n == 0:
                matriz[i][x] = int(input('[{},{}]> '.format(i, x)))
            else:
                print(f'[{matriz[i][x]:5}]', end='')
                if x == 2:
                    print()

input() #wait