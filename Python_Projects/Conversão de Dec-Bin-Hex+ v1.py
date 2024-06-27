while True:
    print ("[01] - Decimal para Binário;")
    print ("[02] - Binário para Decimal;")
    print ("[03] - Decimal para Hexadecimal;")
    print ("[04] - Hexadecimal para Decimal;")
    print ("[05] - Binário para Hexadecimal;")
    print ("[06] - Hexadecimal para Binário;")
    print ("[07] - Outra base.")
    option = int (input ("What operation will be done?_ "))

###################################################
    def dec_bin(number): #Decimal para Binário
        lisX = []
        result = int(number)
        while result != 1:
            aux_var = result % 2
            if aux_var > 0 and aux_var < 1:
                aux_var = 1
            lisX.insert (0, aux_var)
            result = result // 2     
        lisX.insert (0, result)

        return lisX
###################################################
    def bin_dec(number): #Binário para Decimal
        lisX = []
        for i in number:
            i = int(i)
            lisX.append (i)     
        m = 1
        soma = 0
        for i in number:
            i = int(i)
            soma = soma + i*2**(len(lisX) - m)
            m += 1
        
        return soma
###################################################
    def dec_hex(number): #Decimal para Hexadecimal
        lista = []
        number = int(number)
        while number > 15:
            resto = number % 16
            number = number // 16
            lista.insert(0, resto)
            
        lista.insert(0, number)
        count = -1
        for i in lista:
            count += 1
            if i != 10 and i != 11 and i != 12 and i != 13 and i != 14 and i != 15:
                continue
            elif i == 10:
                lista[count] = "A"
            elif i == 11:
                lista[count] = "B"
            elif i == 12:
                lista[count] = "C"
            elif i == 13:
                lista[count] = "D"
            elif i == 14:
                lista[count] = "E"
            elif i == 15:
                lista[count] = "F"
                
        return lista
###################################################
    #def hex_dec(number): #Hexadecimal para Decimal
        




###################################################

    if option == 7:
        base = int(input("Informe a base do número que será convertido.\nBase: "))
        number = input("Digite o número: ")
        #####continuo depois
    elif option > 0 and option < 7:
        number = (input("Enter a number: "))
        if option == 1:
            for i in range (len(dec_bin(number))):
                print (dec_bin(number)[i], end="")
            print ("\n")
        elif option == 2:
            print (bin_dec(number),"\n")
        elif option == 3:
            for i in range (len(dec_hex(number))):
                print (dec_hex(number)[i], end="")
            print ("\n")
        elif option == 4:
            print ("Em desenvolvimento")
        elif option == 5:
            print ("Em desenvolvimento")
        elif option == 6:
            print ("Em desenvolvimento")
    else: print ("Opção inválida!\n")

