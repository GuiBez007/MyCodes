setence = input("Insert your phrase: \n")

lisT = []
new_lisT = []

for letter in setence:
    letter = letter.upper()
    if letter == " " or letter == "," or letter == ".":
        continue
    lisT.append(letter)
    
for element in lisT:
    new_lisT.insert(0,element)
    
for count in range(len(lisT)):
    condiction = True
    if lisT[count] != new_lisT[count]:
        print("\nIt's not a palindrome!:(")
        condiction = False
        break
    
if condiction == True:
    print("\nIt's a palindrome!:)")

input()
