# Write a program that has a function called grades() that can receive multiple student grades and return
# a dictionary with the following information:
# - Quantity of grades
# - The highest
# - The lowest
# - The class average
# - The situation (optional)

def grades(student_grades, situation=False):
    """
    -> A function responsible for show a short information board about the students performance 
    :param student_grades: A list with the students grades
    :param situation: An (optional) parameter that describes the class performance 
    :return: Return a dictionary with grades quantity, highest, lowest, class average and situation
    """""
    length = len(student_grades)
    highest = max(student_grades)
    lowest = min(student_grades)
    average = sum(student_grades) / length

    dictionary = {'length': length,
                  'highest': highest,
                  'lowest': lowest,
                  'average': average}

    if situation:
        if average >= 7:
            dictionary['situation'] = 'GOOD!'
        elif average >= 5:
            dictionary['situation'] = 'AVERAGE!'
        else:
            dictionary['situation'] = 'BAD!'
    return dictionary


# main()
student_grades = []
print('===== Inform the student grades to get more info [S to STOP] =====')
while True:
    grade = input('GRADE> ')
    if grade[0] in 'Ss':
        break
    elif not grade[0].isnumeric():
        continue
    student_grades.append(float(grade))

print(grades(student_grades, True))
help(grades)

input() #wait