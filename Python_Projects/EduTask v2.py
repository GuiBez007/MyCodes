#Name: Without a name :(
#Author: Friends that we make in the way ..XD:Lmao
#Date: 15/05/2023 15:??
#Descryption: Adivinha o número que o usuário está pensando, por meio de perguntas.

print ("Think a number!")
answer = input ("Your number its < 50 ?\n")
one_hundred = 100
z = 0

if answer == "yes" or answer == "y": 
    new_number = 25     #new=25
    last_number = 50    #last=50
else: #answer == "no":
    new_number = 75     #new=75
    last_number = 50    #last=50

for i in range (9):    
    print ("\nYour number its <",new_number,"?")
    answer = input ()
    if answer == "yes":             #caso seja menor que o novo número
        third_var = new_number
        new_number = (last_number - new_number)
        if new_number < 0: #positivador
            new_number = new_number * -1
            
        if new_number < 4:
            for x in range (5):
                third_var = third_var - 1
                print ("\nYour number its =",third_var,"?")
                answer = input ()
                if answer == "yes":
                    print ("\nThe number you thought of was", third_var)
                    z = 1
                    break
        if z != 0:
            break
                   
        new_number = third_var - new_number // 2
        last_number = third_var
        
    else: #answer == "no":          #caso seja maior que o novo número
            third_var = new_number
            new_number = (last_number - new_number)
            if new_number < 0: #positivador
                new_number = new_number * -1
                    
            if new_number < 4:
                fourth_var = third_var
                for x in range (1,6):
                    third_var = fourth_var + (x-1) 
                    print ("\nYour number its =",third_var,"?")
                    answer = input ()
                    if answer == "yes":
                        print ("\nThe number you thought of was", third_var)
                        z = 1
                        break
            if z != 0:
                break
            
            new_number = third_var + new_number // 2
            last_number = third_var

input() #pause
