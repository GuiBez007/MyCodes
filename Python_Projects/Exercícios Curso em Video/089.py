# Write a code that reads name and two grades of various students and put it in a composite list. At the end,
# show a report card contain each average and allow user to show the grades of each student individually.

grades = [[], []]
aux = []
count = 1

print('Inform below the students\' grades [S to STOP]: ')
while True:
    name = input(f'{count}° student\'s name> ')
    if name in 'Ss':
        break
    grades[0].append(name)

    for i in range(1, 3):
        aux.append(float(input(f'- {i}° grade> ')))
    print()

    grades[1].append(aux[:])
    aux.clear()
    count += 1

print('\n=== STUDENTS\' REPORT CARD ===')
print('num   name        average')
for i in range(len(grades[0])):
    print('{:3}   {:11} {:4.2f}'.format(i+1, grades[0][i], (grades[1][i][0]+grades[1][i][1]) / 2))
print('='*29)

print('\nInform the student\'s number you wanna see the grades: ')
while True:
    student = int(input('NUMBER> '))
    if student in range(len(grades[0])+1):
        print('The student {} grades are {} \n'.format(grades[0][student-1], grades[1][student-1]))

input() #wait