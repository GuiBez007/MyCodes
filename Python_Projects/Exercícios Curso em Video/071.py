# Write a code that simulates the working of a cash machine. At begin, ask user what's the value that will be
# withdrawn (integer number) and the program will inform how many parcels for each value will be sent.
# OBS> consider that the cash machine has banknotes of R$(50/20/10/1).

withdraw = int(input('Inform the withdraw value: '))
print('Will be necessary:')
note_50 = note_20 = note_10 = rest = 0

while True:
    if withdraw >= 50:
        rest = withdraw % 50
        note_50 = withdraw // 50
        print('{:2} R$50,00 notes'.format(note_50))
    elif withdraw >= 20:
        rest = withdraw % 20
        note_20 = withdraw // 20
        print('{:2} R$50,00 notes'.format(note_20))
    elif withdraw >= 10:
        rest = withdraw % 10
        note_10 = withdraw // 10
        print('{:2} R$50,00 notes'.format(note_10))

    if withdraw == rest:
        print('{:2} R$01,00 notes'.format(rest))
        break
    withdraw = rest

input() #wait