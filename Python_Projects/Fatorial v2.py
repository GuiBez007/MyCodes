#Name: Fatorial
#Author: GUilherme Bezerra
#Date: ??/05/2023 ??:??
#Description: Calcula fatorial de números inteiros

def fatorial(number):
    temp = 1
    for i in range(1,number):
        print(temp, '*', i, '=', temp*(i+1))
        temp *= (i+1)
    return temp
    
number = int(input('Number: '))
print ('The factorial of the number',number,'is',fatorial(number))

input() #pause
