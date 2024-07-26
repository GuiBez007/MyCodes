# Create a module called M107.py that has the functions increase(), decrease(), double() and half().
# Make a program that imports this module and use some of these functions.

from usefulCeV.ex107 import M107

price = int(input('Inform the price> '))
print(f'INCREASE by 10% -> {M107.increase(price, 10)} \n'
      f'DECREASE by 10% -> {M107.decrease(price, 10)} \n'
      f'DOUBLE -> {M107.double(price)}                     \n'
      f'HALF -> {M107.half(price)}                          ')

input() #wait