num0 = ["###","# #","# #","# #","###"]
num1 = ["  #","  #","  #","  #","  #"]
num2 = ["###","  #","###","#  ","###"]
num3 = ["###","  #","###","  #","###"]
num4 = ["# #","# #","###","  #","  #"]
num5 = ["###","#  ","###","  #","###"]
num6 = ["###","#  ","###","# #","###"]
num7 = ["###","  #","  #","  #","  #"]
num8 = ["###","# #","###","# #","###"]
num9 = ["###","# #","###","  #","###"]

number = input("Insert a number: ")
for vezes in range(5):
    num = ""
    for i in number:
        if i == '0':
            if vezes+1 == 1:
                num = num + " " + num0[0]
            elif vezes+1 == 2:
                num = num + " " + num0[1]
            elif vezes+1 == 3:
                num = num + " " + num0[2]
            elif vezes+1 == 4:
                num = num + " " + num0[3]
            elif vezes+1 == 5:
                num = num + " " + num0[4]
        elif i == '1':
            if vezes+1 == 1:
                num = num + " " + num1[0]
            elif vezes+1 == 2:
                num = num + " " + num1[1]
            elif vezes+1 == 3:
                num = num + " " + num1[2]
            elif vezes+1 == 4:
                num = num + " " + num1[3]
            elif vezes+1 == 5:
                num = num + " " + num1[4]
        elif i == '2':
            if vezes+1 == 1:
                num = num + " " + num2[0]
            elif vezes+1 == 2:
                num = num + " " + num2[1]
            elif vezes+1 == 3:
                num = num + " " + num2[2]
            elif vezes+1 == 4:
                num = num + " " + num2[3]
            elif vezes+1 == 5:
                num = num + " " + num2[4]
        elif i == '3':
            if vezes+1 == 1:
                num = num + " " + num3[0]
            elif vezes+1 == 2:
                num = num + " " + num3[1]
            elif vezes+1 == 3:
                num = num + " " + num3[2]
            elif vezes+1 == 4:
                num = num + " " + num3[3]
            elif vezes+1 == 5:
                num = num + " " + num3[4]
        elif i == '4':
            if vezes+1 == 1:
                num = num + " " + num4[0]
            elif vezes+1 == 2:
                num = num + " " + num4[1]
            elif vezes+1 == 3:
                num = num + " " + num4[2]
            elif vezes+1 == 4:
                num = num + " " + num4[3]
            elif vezes+1 == 5:
                num = num + " " + num4[4]
        elif i == '5':
            if vezes+1 == 1:
                num = num + " " + num5[0]
            elif vezes+1 == 2:
                num = num + " " + num5[1]
            elif vezes+1 == 3:
                num = num + " " + num5[2]
            elif vezes+1 == 4:
                num = num + " " + num5[3]
            elif vezes+1 == 5:
                num = num + " " + num5[4]
        elif i == '6':
            if vezes+1 == 1:
                num = num + " " + num6[0]
            elif vezes+1 == 2:
                num = num + " " + num6[1]
            elif vezes+1 == 3:
                num = num + " " + num6[2]
            elif vezes+1 == 4:
                num = num + " " + num6[3]
            elif vezes+1 == 5:
                num = num + " " + num6[4]
        elif i == '7':
            if vezes+1 == 1:
                num = num + " " + num7[0]
            elif vezes+1 == 2:
                num = num + " " + num7[1]
            elif vezes+1 == 3:
                num = num + " " + num7[2]
            elif vezes+1 == 4:
                num = num + " " + num7[3]
            elif vezes+1 == 5:
                num = num + " " + num7[4]
        elif i == '8':
            if vezes+1 == 1:
                num = num + " " + num8[0]
            elif vezes+1 == 2:
                num = num + " " + num8[1]
            elif vezes+1 == 3:
                num = num + " " + num8[2]
            elif vezes+1 == 4:
                num = num + " " + num8[3]
            elif vezes+1 == 5:
                num = num + " " + num8[4]
        elif i == '9':
            if vezes+1 == 1:
                num = num + " " + num9[0]
            elif vezes+1 == 2:
                num = num + " " + num9[1]
            elif vezes+1 == 3:
                num = num + " " + num9[2]
            elif vezes+1 == 4:
                num = num + " " + num9[3]
            elif vezes+1 == 5:
                num = num + " " + num9[4]
    print(num)

input('Press <enter> to continue!')
