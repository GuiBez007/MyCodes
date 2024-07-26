# Create a package called usefulCeV that has two intern modules called coin and data. Transfer all functions used
# in the challenges 107-109 for the first package and keep everything working.

from usefulCeV import coin
price = float(input('Inform the price> '))
coin.resume(price, True, 10, 10)

input() #wait