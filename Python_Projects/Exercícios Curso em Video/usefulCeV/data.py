def readMoney(text):
    while True:
        price = input(f'{text}')
        price = price.replace(',', '.')

        if price.replace('.', '').isnumeric():
            return float(price)
        print('\033[31mInvalid value! \033[m\n')