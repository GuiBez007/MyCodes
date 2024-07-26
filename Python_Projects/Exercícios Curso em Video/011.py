#Write a code that will read the height and the width of a wall and print the area and the quantity of ink
#knowing each liter of ink paint an area of 2m²

height = float(input('Type the wall\'s height: '))
width = float(input('Now, the wall\'s width: '))

necessary_ink = (height * width) / 2
print('The total area is {:.2f} and will be necessary {:.2f} liters of ink!'\
      .format(height * width, necessary_ink))

input() #wait
