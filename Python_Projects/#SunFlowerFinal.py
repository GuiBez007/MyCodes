def Comprar(tipo_picareta, quantidade):

    machado =          [20, 0, 0, 0]
    picareta_madeira = [20, 3, 0, 0]
    picareta_pedra =   [20, 3, 5, 0]
    picareta_ferro =   [80, 3, 0, 5]

    # Calcúlo de resursos da picareta de madeira
    picareta_madeira[0] = picareta_madeira[0] + (machado[0] * 3)

    # Calcúlo de resursos da picareta de pedra
    picareta_pedra[1] = picareta_pedra[1] + (picareta_madeira[1] * 5)
    picareta_pedra[0] = picareta_pedra[0] + (picareta_madeira[0] * 5) + (machado[0] * 3)

    # Calcúlo de resursos da picareta de ferro
    picareta_ferro[2] = picareta_pedra[2] * 5
    picareta_ferro[1] = picareta_ferro[1] + (picareta_pedra[1] * 5)
    picareta_ferro[0] = picareta_ferro[0] + (picareta_pedra[0] * 5) + (machado[0] * 3)


    # retorno de cada picareta
    if tipo_picareta == 'madeira':
        picareta_madeira[0] = picareta_madeira[0] * quantidade
        picareta_madeira[1] = picareta_madeira[1] * quantidade
        return picareta_madeira

    elif tipo_picareta == 'pedra':
        picareta_pedra[0] = picareta_pedra[0] * quantidade
        picareta_pedra[1] = picareta_pedra[1] * quantidade
        picareta_pedra[2] = picareta_pedra[2] * quantidade
        return picareta_pedra

    elif tipo_picareta == 'ferro':
        picareta_ferro[0] = picareta_ferro[0] * quantidade
        picareta_ferro[1] = picareta_ferro[1] * quantidade
        picareta_ferro[2] = picareta_ferro[2] * quantidade
        picareta_ferro[3] = picareta_ferro[3] * quantidade
        return picareta_ferro



# main()
ferramenta = input('Que ferramenta deseja criar (M/P): ')

if ferramenta == 'm' or ferramenta == 'M':
    quantidade = int(input('Quantos machados deseja: '))
    machado = quantidade * 20
    print('O total a ser pago é de {}'.format(machado))

else:
    tipo_picareta = input('Digite que tipo de picareta deseja! Caso necessário, informe uma quantidade (EX:Pedra 4): ')
    opcao = tipo_picareta.split()

    if len(opcao) != 2:
        opcao.append(1)

    total = Comprar(opcao[0], int(opcao[1]))
    print('\nO TOTAL DE MATERIAIS É: \nOuro Total -> {} \nTroncos -> {} \nPedras -> {} \nFerros -> {}'.format(total[0], total[1], total[2], total[3]))

input()
