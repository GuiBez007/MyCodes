ist = []
lis = []
vezes = int(input('Quantity of numbers to be add in the list: '))

#pega a quantidade de números que o usuário digitará
i = 0
while i < vezes:
    ist.append (int(input('Enter the number: ')))
    i += 1
print ('\nOriginal list ->', ist)

#organiza do maior número ao menor e mostra na tela
i = 0
for x in range (len(ist)):
    largest_number = ist[0]
    while i < len(ist):
        if ist[i] > largest_number:
            largest_number = ist[i]
        i += 1
    lis.append(largest_number)
    
    y = 0
    while y < len(ist):
        if largest_number == ist[y]:
            del ist[y]
            break
        y += 1
    i = 0
print (' Ordened list ->', lis)
input('\nPress <enter> to continue!')
