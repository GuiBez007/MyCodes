# Write a program that can reads the distance of a travel and inform his cost to user

distance = float(input('What\'s the travel distance in KM: '))
if distance > 200:
    print('The cost of this travel will be ${:.2f}'.format(distance * 0.45))
else: print('The cost of this travel will be ${:.2f}'.format(distance * 0.50))

input() #wait