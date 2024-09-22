# Name: POO_training_1
# Author: GUilherme Bezerra
# Date: 06/08/2024 16:00h
# Description: A program that reads 4 grades of an uncertain quantity of students and shows their average.

class Student:
    def __init__(self, name):
        self.name = name.capitalize()
        self.grades_list = self.grades()
        self.sum = sum(self.grades_list)


    @staticmethod
    def grades():
        order = ['first', 'second', 'third', 'fourth']
        grades = []
        for i in range(4):  # get the four student grades
            grades.append(float(input(f'- {order[i]} grade> ')))
        return grades


# this function analyses if user want to stop the execution or not
def stopVerification(name, students_list):
    if name.upper() in 'STOP':
        print(f'{c(1)}Program was finished!{c(9)}')
        return False
    students_list.append(Student(name))  # instance of students
    return True


def c(color):
    return f'\033[3{color}m'


# main()
def main():
    students_list = []
    print('\033[7mStudent grades program! [S to STOP]\033[m')

    while True:
        if not stopVerification(input('Student name> '), students_list):
            break
        print()

    print('\n\033[7m=== Average of each student ===\033[m')
    for i in range(len(students_list)):
        aux = students_list[i]
        if aux.sum / 4 < 4:
            print(c(1), end='')
        elif aux.sum / 4 < 7:
            print(c(3), end='')
        else:
            print(c(2), end='')
        print('The average of {} was {:.2f}'.format(aux.name, aux.sum / 4), end='')  # OUTPUT
        print(c(9))


if __name__ == '__main__':
    main()