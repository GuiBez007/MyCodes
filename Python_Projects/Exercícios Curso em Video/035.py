# Write a program that reads 3 values and inform if it can do a triangle or not

print('-=-' * 20, '\n{}TRIANGLE ANALYSIS\n'.format(' ' * 20), '-=-' * 20)
straight_1 = float(input('Type the length of the FIRST straight: '))
straight_2 = float(input('Type the length of the SECOND straight: '))
straight_3 = float(input('Type the length of the THIRD straight: '))

#if straight_1 + straight_2 > straight_3 and straight_2 + straight_3 > straight_1 and straight_3 + straight_1 > straight_2:
# Very better form above
if straight_1 + straight_2 > straight_3:
    if straight_2 + straight_3 > straight_1:
        if straight_3 + straight_1 > straight_2:
            print('A triangle CAN BE FORMED with these straights!')
        else: print('With this sizes a triangle CANNOT be formed!')
    else: print('With this sizes a triangle CANNOT be formed!')
else: print('With this sizes a triangle CANNOT be formed!')

input() #wait