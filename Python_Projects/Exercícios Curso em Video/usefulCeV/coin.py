# Create a module called M107.py that has the functions increase(), decrease(), double() and half().
# Make a program that imports this module and use some of these functions.

def increase(money, rate):
    return money + (money * rate / 100)


def decrease(money, rate):
    return money - (money * rate / 100)


def double(money):
    return money * 2


def half(money):
    return money / 2


# 108.py
def coin(money, format=True):
    #return f'{money:.2f}'.replace('.', ',')
    if format:
        money = str(money)
        aux = []
        for i in money:
            if i == '.':
                aux.append(',')
            else:
                aux.append(i)
        aux.append('0')
        aux = ''.join(aux)
        i = aux.index(',')
        return f'R${aux[:(i+3)]}'
    return money


def resume(money, format=True, x=10, y=10):
    print(f'INCREASE by 10% -> {coin(increase(money, x), format)}')
    print(f'DECREASE by 10% -> {coin(decrease(money, y), format)}')
    print(f'DOUBLE -> {coin(double(money), format)}')
    print(f'HALF -> {coin(half(money), format)}')