#Write an algorithm that will read a cost of product and print the new value with 5% of discount

cost = float(input('Type the cost of product: '))
cost = cost - ((cost /100) *5)
print('The new value of product with 5% of discount is {:.2f}'.format(cost))

input() #wait
