# Create a bank system using classes.

count = 0


class Bank:
    def __init__(self, name):
        self.name = name

    def createAccount(self):
        pass

    def accessAccount(self):
        pass

    def changePassword(self):
        pass

    def depositMoney(self):
        pass

    def withdrawMoney(self):
        pass


def nameVerification(users):
    while True:
        name = input('Inform your name> ').strip().capitalize()
        try:
            int(name)
        except:
            users.append(Bank)  # instance of user
            break
        else:
            print('\033[31mInvalid, try again! \n \033[m')


def optionsMenu(users):
    print('How do you want to proceed?')
    print('[01] - create account;    \n'
          '[02] - access account;    \n'
          '[03] - change password.    ')
    option = int(input('OPTION> '))

    # if option == 1:
    #     users[]
    # elif option == 2:
    # elif option == 3: