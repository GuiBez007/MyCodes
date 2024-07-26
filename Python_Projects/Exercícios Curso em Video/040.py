# Write a program that reads two student grades and calculate their average, showing a message -at the end-:
# lower to 5.0 disapproved / between 5.0 and 6.9 recovery / upper to 7.0 approved

student_1 = float(input('Inform the first student grade: '))
student_2 = float(input('Inform the second student grade: '))
average = (student_1 + student_2) / 2

if average < 5.0:
    print('You\'re DISAPPROVED! Your average> {:.1f}'.format(average))
elif average > 7:
    print('You\'re APPROVED! Your average> {:.1f}'.format(average))
else:
    print('You\'re in RECOVERY! Your average> {:.1f}'.format(average))

input() #wait