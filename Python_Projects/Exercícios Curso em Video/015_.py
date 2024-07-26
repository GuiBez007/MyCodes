#Write a program that asks how much kilometers was passed by a not own car and how many days have passed too.
#Calculate the price knowing the car cost R$60/d and R$0,15/Km passed.

KM = float(input('How many kilometers have you passed with the car?: '))
days = int(input('And how many days have passed since you got the car?: '))

price = (60 * days) + (0.15 * KM)
print('You must to pay R${:.2f} for the car!'.format(price))

input() #wait
