# Write a code that reads the weight of 5 people. At the end, show what was the higher and the lower weight read.

for i in range(5):
    weight = float(input('{}# Type your weight: '.format(i)))
    if i == 0:
        higher = weight
        lower = weight

    if weight > higher:
        higher = weight
    if weight < lower:
        lower = weight

print('The higher weight is {:.2f} and the lower is {:.2f}.'.format(higher, lower))

input() #wait