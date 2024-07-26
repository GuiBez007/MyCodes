import re

import usefulCeV.ex115.interface as interface


def fileExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createFile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('There was an error during the creating of file!')



def writeFile(name):
    try:
        a = open(name, 'at')
    except:
        print('There was an error during the reading of file!')
    else:
        interface.mold('PEOPLE REGISTER')
        name = input('name> ').strip()
        while True:
            age = input('age> ')
            if age.isnumeric():
                break
            else:
                print(f'{interface.c(1)}Invalid, try again!\n{interface.c()}')
        try:
            a.write(f'{name};{age}\n')
        except:
            print('An {}error{} was found while register into the file!'.format(interface.c(1), interface.c()))
        else:
            print('The person {}{} was registered{} successfully!'.format(interface.c(2), name.upper(), interface.c()))
    finally:
        a.close()


def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('There was an error during the reading of file!')
    else:
        interface.mold('REGISTERED PEOPLE')
        while True:
            content = a.readline()
            if not content:
                break
            content = content.strip().split(';')
            length = len(content[0]) + len('years old')
            print(f'{content[0]}{content[1]:>{40 - length}} years old')
    finally:
        a.close()

        # ANTERIOR FUNCIONAL
        # lisT = re.split(r'[;\n]', content)
        # count = 1
        # for i in lisT:
        #     if i == '':
        #         continue
        #
        #     if count == 1:
        #         print(i, end='')
        #         tam = 30 - len(i)
        #         count += 1
        #     else:
        #         print(f'{i:>{tam}}')
        #         count -= 1