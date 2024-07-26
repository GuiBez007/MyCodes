# Develop a logic that reads the weight and the length of a person, calculate his IMC and show his status:
# IMC lower of 18,5 = below of the weight;
# IMC between 18,5 and 25 = correct weight;
# IMC between 25 and 30 = above the right weight;
# IMC between 30 and 40 = obesity
# IMC above 40 = morbid obesity

weight = float(input('Inform your weight: '))
length = float(input('Now, your length: '))
IMC = weight / (length ** 2)

print('Your IMC is {:.2f} so you are '.format(IMC), end='')
if IMC < 18.5:
    print('below of the weight!')
elif IMC < 25:
    print('in the correct weight!')
elif IMC < 30:
    print('above the right weight!')
elif IMC < 40:
    print('in the obesity grade!')
else:
    print('in the morbid obesity grade!')

input() #wait