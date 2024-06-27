# Weekly clan + weekly BossGuild + (weekly diretives)
guild_coin = 3000 + 2500 + (7*500)

#   14/14 - 8/20 -  2/6  -  2/13
# (Bastium/Celano/Avilius/Tronetel) + bônusBossRaid + (weeklyBossRaid)
contribuition_coin = 7*(100+120+50+75) + 500 + (7*100)


def guildCoin(need, have=0): # GUILD COINS FUNCTION
    days = 0
    values = []

    while have < need:
        have += 500    # diretives daily value
        days += 1
        values.append(500)

        if (days % 7) == 0:
            have += 5500
            values.append(5500)

    soma = 0
    print()
    for i in range(len(values)):
        soma += values[i]

        if i == len(values)-1:
            print('{} = {}'.format(values[i], soma))
        else:
            if (i % 8) == 0 and i != 0:
                print()   # line break

            print(values[i], end='+')

    return days


def contribuitionCoin(need, have=0): # CONTRIBUITION COINS FUNCTION
    days = 0
    values = []

    while have < need:
        have += (100+120+50+75) + 100   # coins daily value
        days += 1
        values.append((100+120+50+75) + 100)

        if (days % 7) == 0:
            have += 500
            values.append(500)

    soma = 0
    print()
    for i in range(len(values)):
        soma += values[i]

        if i == len(values) - 1:
            print('{} = {}'.format(values[i], soma))
        else:
            if (i % 8) == 0 and i != 0:
                print()    # line break

            print(values[i], end='+')

    return days


def market():
    while True:
        # LIMPAR TELA AQUI
        bought = float(input('Bought value: '))
        recommended = bought * 0.09 ###

        if bought == -1: # leave
            return

        while True:
            print('\nRecommended> {:.0f}'.format(recommended + bought))
            value = float(input('Value to sell: '))

            if value == -1: # leave
                print()
                break

            total = value - (value * 0.05) # market rate
            if total > bought:
                print('PROFIT> ', end='')
            else:
                print('PREJUDICE> ', end='')

            print('{:.0f}-{:.0f} = {:.0f}vdia'.format(total, bought, total-bought))


# main()
while True:
    # LIMPAR TELA AQUI
    print('- weekly guild coin: {} \n'
          '- weekly contribuition coin: {}\n'.format(guild_coin, contribuition_coin) + '='*35)

    print('[01] - Guild Coin;\n'
          '[02] - Contribuition Coin;\n'
          '[03] - Market. \n' + '='*35)
    option = int(input('I want to know about: '))

    if option == 1:
        value = int(input('How much I\'ll need: '))
        print('Total days to reach the target: {}\n'.format(guildCoin(value)))
    elif option == 2:
        value = int(input('How much I\'ll need: '))
        print('Total days to reach the target: {}\n'.format(contribuitionCoin(value)))
    elif option == 3:
        market()
