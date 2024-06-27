#Name: New Text
#Author: GUilherme Bezerra
#Date: ??/??/???? ??:??
#Description: Change the characteres according with the number 

string = input("Digite seu texto: \n")
x = int(input("Digite um número: "))

text = ''
for i in string:
    if i.isdigit() or i.isspace():
        text = text + i
        continue
    if i.islower():
        i = ord(i) + x
        if i > ord('z'):
            i = ord('a') + (i - ord('z')-1)
    else:
        i = ord(i) + x
        if i > ord('Z'):
            i = ord('A') + (i - ord('Z')-1)
    text = text + chr(i)
print(text)
input()
