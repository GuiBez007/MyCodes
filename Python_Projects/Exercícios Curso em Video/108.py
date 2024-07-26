# Adapt the previous code creating a function named coin() that can show the numbers correctly formatted. EX: R$1234,56

from usefulCeV.ex107 import M107

price = float(input('Inform the price> '))
print(f'INCREASE by 10% -> {M107.coin(M107.increase(price, 10))} \n'
      f'DECREASE by 10% -> {M107.coin(M107.decrease(price, 10))} \n'
      f'DOUBLE -> {M107.coin(M107.double(price))}                     \n'
      f'HALF -> {M107.coin(M107.half(price))}                          ')

input() #wait