secret_number = int(input ("Insert a number: "))

ask = 0
new_number = 50
while ask < 10:
    print ("\nYour number its <", new_number,"?")
    answer = input ("yes or no: ")
    ask += 1
    
    while ask == 1: #SÓ VAI RODAR 1 ÚNICA VEZ
        if answer == "yes": #last == 50 and new == 25
            last_number = new_number
            new_number = new_number // 2
            break 
        elif answer == "no": #last == 50 and new == 75
            last_number = new_number
            new_number = (new_number + 100) // 2
            break
        
    else: #VAI RODAR ENQUANTO A QUANTIDADE DE PERGUNTAS FOR MENOR QUE 10
        if answer == "yes":
            if last_number < new_number:
                third_var = new_number
                new_number = (new_number - last_number)
                if new_number == secret_number:
                    print ("The correct number is:", secret_number,"hehe")
                    break
                if last_number < 1:
                    last_number *= -1
                elif new_number < 1:
                    new_number *= -1
                new_number = new_number // 2 + last_number
                last_number = third_var
                    
            else: #last_number > new_number
                third_var = new_number
                new_number = (new_number - last_number)    
                if last_number < 1:
                    last_number *= -1
                elif new_number < 1:
                    new_number *= -1
                new_number = new_number // 2
                new_number = (third_var - new_number) -1
                last_number = third_var
                if new_number == last_number:
                    new_number = new_number -1
                    
        elif answer == "no":
            if secret_number > 25 and secret_number < 50:     
                third_var = new_number
                new_number = (50 - new_number) // 2 + new_number
                last_number = third_var
                if new_number == secret_number:
                    print ("The correct number is:", secret_number,"hehe")
                    break
                
            elif last_number > new_number:
                third_var = new_number
                new_number = (last_number - new_number)
                if new_number == secret_number and ask > 5:
                    print ("The correct number is:", secret_number,"hehe")
                    break
                last_number = third_var
                if last_number < 1:
                    last_number *= -1
                elif new_number < 1:
                   new_number *= -1
                new_number = new_number // 2 + new_number

            elif last_number < new_number:
                 third_var = new_number
                 new_number = (100 - new_number) // 2 + new_number
                 last_number = third_var
                 if new_number == last_number:
                     new_number = new_number + 1 
                 if new_number == secret_number:
                     print ("The correct number its:", secret_number,"hehe")
                     break
            
    if new_number == secret_number and ask > 5:
        print ("The correct number its:", secret_number,"hehe:)") #bruxaria XD (Wrong!)
        break
else:
    print ("Sorry, we didn't find out the correct number:(")

input() #pause
