#Name: Fibonacci's Sequence
#Author: GUilherme Bezerra
#Date: 21/05/2023 12:18
#Description: Realize the Fibonacci's sequence according the number entered by user

def Fibonacci(number):
    global lisT
    lisT = [1,1]
    for i in range(2, number):
        lisT.append(lisT[i-1] + lisT[i-2])

print('=== FIBONACCI SEQUENCE ===')
number = int(input("Enter a number: "))
Fibonacci(number)
for i in range(number):
    print (i+1,"->",lisT[i])
input()
