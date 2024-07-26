# Write a code that reads a phrase and shows if it's a palindrome or not, without spaces.
# EXAMPLES: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

phrase = input('Type any phrase to check if it\'s a palindrome: ').upper().replace(' ', '')

inverted = ''
for i in range(len(phrase)-1, -1, -1):
    inverted += phrase[i]

if phrase == inverted:
    print('The informed phrase IS a palindrome!')
else:
    print('The informed phrase IS NOT a palindrome!')

input() #wait