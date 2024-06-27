nums = [["###","  #","###","###","# #","###","###","###","###","###"],
        ["# #","  #","  #","  #","# #","#  ","#  ","  #","# #","# #"],
        ["# #","  #","###","###","###","###","###","  #","###","###"],
        ["# #","  #","#  ","  #","  #","  #","# #","  #","# #","  #"],
        ["###","  #","###","###","  #","###","###","  #","###","###"]]


def printNum(number):
    for index in range(5):
        if index != 0:
            print() # next line
            
        for i in number:
            if i == '0':
                print(nums[index][0],end=' ')
            elif i == '1':
                print(nums[index][1],end=' ')
            elif i == '2':
                print(nums[index][2],end=' ')
            elif i == '3':
                print(nums[index][3],end=' ')
            elif i == '4':
                print(nums[index][4],end=' ')
            elif i == '5':
                print(nums[index][5],end=' ')
            elif i == '6':
                print(nums[index][6],end=' ')
            elif i == '7':
                print(nums[index][7],end=' ')
            elif i == '8':
                print(nums[index][8],end=' ')
            elif i == '9':
                print(nums[index][9],end=' ')
# function end



# main()
while True:
    printNum(input('Insert a number: '))
    input('\nPress <enter> to continue! \n')

