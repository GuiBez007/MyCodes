# Into the package usefulCeV we created in challenge 111, we have a module named data. Create a function called
# readMoney() that be able to work as a function input(), but with a data validation to accept just monetary values.

from usefulCeV import coin, data
price = data.readMoney('Inform the price> ')
coin.resume(price, True, 10, 10)

input() #wait