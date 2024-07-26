#Write a code that can convert °C in °F

celsius = float(input('Type the temper in Celsius: °C'))
fahrenheit = (celsius * 1.8) + 32
print('The temper of °C{:.2f} in fahrenheit is: °F{:.2f}'.format(celsius, fahrenheit))

input() #wait
