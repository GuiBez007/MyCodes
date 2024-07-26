#Write a program that reads how much money the person has and print how many dollars the person can have

money = float(input('How much money do you have: '))
dollars = money / 3.27
print('You have US${:.2f}!'.format(dollars))

input() #wait