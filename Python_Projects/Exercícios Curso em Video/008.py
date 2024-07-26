#Write a code that reads a value in meters and convert it to centimeters and millimeters

meters = float(input('Inform the meters: '))
print('In centimeters: {:.2f} \nIn millimeters: {:.2f}'.format(meters*100, meters*1000))

input() #wait
