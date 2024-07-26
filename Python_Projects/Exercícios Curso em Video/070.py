# Write a code that reads the name and the cost of varius products. The program will must ask if user will
# continue or not. At the end, show:
# - What's the total spent in the purchase
# - How many products cost more than R$1000,00
# - What's the name of the cheaper product

count = 1
total_price = exp_products = cheaper_price = 0
cheaper_prod = ''

while True:
    print('======= {}°PRODUCT ======='.format(count))
    name = input('Product\'s name: ')
    price = float(input('Its price: '))

    # check the lowest price
    if count != 1:
        if price < cheaper_price:
            cheaper_price = price
            cheaper_prod = name
    else:
        cheaper_prod = name
        cheaper_price = price

    # get the total and the highest price
    total_price += price
    if price > 1000:
        exp_products += 1

    option = input('To continue[Y/N]: ').strip().upper()
    if option == 'N':
        break

    print()
    count += 1

print('\nThe total of this purchase was {},     \n'
      'there was {} costing more than R$1000,00 \n'
      'and the cheaper product was {}.'.format(total_price, exp_products, cheaper_prod))

input() #wait