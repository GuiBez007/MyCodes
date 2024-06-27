#Name: Infinity Loop?
#Author: GUilherme Bezerra
#Date: 20/08/2023 16:25h
#Description: Tranca-trouxa

import random
password = random.randint(0,10)
print(password)

def password(key):
    #print(password)
    if key == password:
        return True
    return False

print("You're stuck! Try a number between 0-10 to scape from this! \
\nBut be careful! You just have 3 chances:) or else....\n")
lisT = ["First","Second","Third"]

for TRY in range(3):
    print(lisT[TRY],"try:",end=" ")
    answer = int(input())
    if password(answer) == True:
        print("Congratulations! You've won this game!!!")
        break
    if TRY != 2:
        print('NOPE! Try again.\n')
else: print("Sorry, you lose this game. Now, YOUR LIFE IS MINE!!!!!")
input()

    
