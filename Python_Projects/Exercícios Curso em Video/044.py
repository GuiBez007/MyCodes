# Elaborate a program that calculates the value to pay for a product, knowing its normal price and the payment form
# once in cash/check = 10% off
# once in card = 5% off
# until 2x in card = formal price
# 3x or more in card = 20% fees

price = float(input('Product\'s value: '))
print('[01] - cash or check; \n'
      '[02] - once in card; \n'
      '[03] - twice in card; \n'
      '[04] - three times or more in card.')
form = int(input('Please, choice an option: '))

if form == 1:
    print('\nYou\'ve acquired 10% off! \nThe total price to pay is ${:.2f}.'.format(price - (price * 0.1)))
elif form == 2:
    print('\nYou\'ve acquired 5% off! \nThe total price to pay is ${:.2f}.'.format(price - (price * 0.05)))
elif form == 3:
    print('\n{} parcels in {:.2f} with a total price of ${:.2f}.'.format(2, price/2, price))
elif form == 4:
    total = price + (price * 0.2)
    parcels = int(input('Inform the parcels quantity: '))
    print('\nThere is a fee of 20%. \n{} parcels in {:.2f} with a total price of ${:.2f}.'
          .format(parcels, total/parcels, total))

input() #wait