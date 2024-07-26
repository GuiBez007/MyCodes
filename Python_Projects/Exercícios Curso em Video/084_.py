# Read the weight of various people and keep it in a list. Show:
# - How many people was registered
# - A list with the fatter people
# - A list with the thinner people

weights = [[], []]
SLA = [[], []]
fatter = thinner = 0

print('Inform the people\'s weights below [under 0 to stop]: ')
count = 0
while True:
    weights[0].append(str(input(f'{count+1}° person\'s name> ')))
    weights[1].append(float(input(f'{weights[0][count].capitalize()}\'s weight> ')))
    print()

    if count == 0:
        fatter = thinner = weights[1][count]
    elif weights[1][count] < 0:
        break

    if weights[1][count] > fatter:
        fatter = weights[1][count]
    elif weights[1][count] < thinner:
        thinner = weights[1][count]
    count += 1

fatter = weights[1].index(fatter)
thinner = weights[1].index(thinner)
i = fatter

for x in range(2):
    if x == 0:
        while i < count:
            if weights[1][i] == weights[1][fatter]:
                SLA[0].append(weights[0][i])
            i += 1
        i = thinner
    else:
        while i < count:
            if weights[1][i] == weights[1][thinner]:
                SLA[1].append(weights[0][i])
            i += 1

print(f'\nThere was {count} registered people in total!')
print(f'The fattest people were {SLA[0]} with weight {weights[1][fatter]}')
print(f'The thinner people were {SLA[1]} with weight {weights[1][thinner]}')

input() #wait