#COD-Secret
#Description: unknown
import os
while True:
    option = input("COD/cod: ")
    if option == "COD":
        text = input()
        lisT = []
        os.system("cls")
        for char in text:
            if char == 'a' or char == 'á' or char == 'à' or char == 'â' or char == 'ã':
                lisT.insert(0,'1')
                continue
            elif char == 'e' or char == 'é' or char == 'è' or char == 'ê':
                lisT.insert(0,'5')
                continue
            elif char == 'i' or char == 'í' or char == 'ì':
                lisT.insert(0,'9')
                continue
            elif char == 'o' or char == 'ó' or char == 'ô' or char == 'ò' or char == 'õ':
                lisT.insert(0,'6')
                continue
            elif char == 'u' or char == 'ú' or char == 'ù':
                lisT.insert(0,'3')
                continue
            elif char == " ":
                continue
            lisT.insert(0,char)
        for i in lisT:
            print(i, end="")
        print ("\n")
    elif option == "cod":
        text = input()
        lisT = []
        os.system("cls")
        for char in text:
            if char == '1':
                lisT.insert(0,'a')
                continue
            elif char == '5':
                lisT.insert(0,'e')
                continue
            elif char == '9':
                lisT.insert(0,'i')
                continue
            elif char == '6':
                lisT.insert(0,'o')
                continue
            elif char == '3':
                lisT.insert(0,'u')
                continue
            lisT.insert(0,char)
        for i in lisT:
            print (i, end="")
        print ("\n")
    else: 
        print ("ERROR")
        break
