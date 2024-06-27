#Name: Fatorial
#Author: GUilherme Bezerra
#Date: 21/05/2023 11:52
#Description: Calcula fatorial de números inteiros

def fatorial(number):
    if number < 0:
        return None
    elif number < 2:
        return 1
    
    fatorial_soma = number
    for i in range(number, 1, -1):
        temp = fatorial_soma
        fatorial_soma = fatorial_soma*(i-1)
        print (temp,"*",i-1,"=",fatorial_soma)
    return fatorial_soma
    
number = int(input("Enter the number that will be factoried: "))
print ("Result =", fatorial(number))

input() #pause
