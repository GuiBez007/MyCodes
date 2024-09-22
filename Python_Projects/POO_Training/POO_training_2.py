# Create a bank system using classes.
from POO_directories.POO_training_2_MODULE import *
from POO_directories.POO_training_2_MODULE import note_block as nt

def main():
    users = []
    nameVerification(users)
    # optionsMenu(users)
    nt.readFile('teste.txt')


if __name__ == '__main__':
    main()