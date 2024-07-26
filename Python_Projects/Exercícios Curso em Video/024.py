# Write a code that reads a city's name and print if this city has the word 'Santo' in his first name

city_name = input('Type the name of the city: ')
print('This city begins with "Santo": {}'.format('SANTO' in ((city_name.upper()).split())[0]))

input() #wait