# Write a program that reads the car's speed and print if it has been fined or not

speed = float(input('Type the car\'s speed: '))
if speed > 80:
    penalty = (speed - 80) * 7
    print('You\'ve been fined in ${:.2f}'.format(penalty))
else:
    print('You\'re okay!')

input() #wait