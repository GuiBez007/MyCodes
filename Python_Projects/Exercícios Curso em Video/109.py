# Modify the functions that has created previously so that they can accept one more parameter, informing if their
# returned value will be formatted or not by function coin().

from usefulCeV.ex107 import M107

price = float(input('Inform the price> '))
print(f'INCREASE by 10% -> {M107.coin(M107.increase(price, 10), format)}')
print(f'DECREASE by 10% -> {M107.coin(M107.decrease(price, 10), format)}')
print(f'DOUBLE -> {M107.coin(M107.double(price), format)}')
print(f'HALF -> {M107.coin(M107.half(price), False)}')

input() #wait