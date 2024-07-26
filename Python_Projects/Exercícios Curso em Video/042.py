# Write a code that inform what kind of triangle will be done (exercise 35 continuation):
# equilateral (all sides equals), isosceles (two sides equals and one different), scalene (all sides different)

straight_1 = float(input('Type the first straight: '))
straight_2 = float(input('Type the second straight: '))
straight_3 = float(input('Type the third straight: '))

if straight_1 + straight_2 > straight_3 and straight_2 + straight_3 > straight_1 and straight_3 + straight_1 > straight_2:
    print('The formed triangle was ', end='')
    if straight_1 == straight_2 or straight_1 == straight_3 or straight_2 == straight_3:
        if straight_1 == straight_2 and straight_2 == straight_3:
            print('EQUILATERAL!')
        else:
            print('ISOSCELES!')
    else:
        print('SCALENE!')
else:
    print('It\'s NOT POSSIBLE to create a triangle with informed straights!')

input() #wait