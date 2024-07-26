# Add into the module M107.py created previously, a function named resume(), that shows in the screen some information
# created by functions that we ever have in the module.

from usefulCeV.ex107 import M107

price = float(input('Inform the price> '))
M107.resume(price, True, 10, 10)

input() #wait