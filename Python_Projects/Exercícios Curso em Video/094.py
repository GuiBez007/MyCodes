# Create a program that reads name, sex and age of various people, keeping the stats of each person in a dictionary
# and all dictionaries in a list. At the end show:
# - How many people were registered
# - The age average
# - A list with all women
# - A list of people with age above average

information = []
age_average = 0

print('=== Register the information of the people below [S to STOP] ===')
while True:
    person = {'name': input('NAME> ').strip()}
    if person['name'] in 'Ss':
        break
    person['age'] = int(input('AGE> ').strip())
    person['sex'] = input('SEX [M/F]> ').strip().upper()[0]
    if person['sex'] not in 'MF':
        print('Invalid Information! \n')
        continue
    print()

    information.append(person)
    age_average += person['age']
age_average /= len(information)

print('\n============== RESULT ===============')
print(f'There are a total of {len(information)} people registered')
print(f'The age average of these people is {age_average:.2f}')

print('The registered women were', end=' ')
for i in range(len(information)):
    if information[i]['sex'] == 'F':
        print(information[i]['name'], end=' ')

print('\nThe people with age above the average are', end=' ')
for i in range(len(information)):
    if information[i]['age'] > age_average:
        print(information[i]['name'], end=' ')

input() #wait