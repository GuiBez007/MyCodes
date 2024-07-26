# Do a program that has a function named write(), that receive a text as parameter and shows an adaptation length message.
# EX: write('Amoeba')
# EXIT: ~~~~~~
#       Amoeba
#       ~~~~~~

def write(text):
    length = len(text)
    print('~' * (length + 4))
    print(f'  {text}  ')
    print('~' * (length + 4))


# main()
while True:
    text = input('Type something> ')
    write(text)

input() #wait