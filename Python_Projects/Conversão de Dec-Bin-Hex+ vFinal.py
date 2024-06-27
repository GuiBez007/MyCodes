#Name: Conversor Numérico
#Author: GUilherme Bezerra
#Date: 22/05/2023 19:44
#Description: Converte os números de acordo com as bases escolhidas

import os
while True:
    print ("[00] - Limpar a tela;")
    print ("[01] - Decimal para Binário;")
    print ("[02] - Binário para Decimal;")
    print ("[03] - Decimal para Hexadecimal;")
    print ("[04] - Hexadecimal para Decimal;")
    print ("[05] - Binário para Hexadecimal;")
    print ("[06] - Hexadecimal para Binário;")
    print ("[07] - Outra base.")
    option = int (input ("What operation will be done?_ "))
    
    if option == 0:
        os.system("cls")
        continue

###################################################################
    def dec_for_all_bases(number,base): #Decimal para qualquer base
        lista = []
        number = int(number)
        while number > base-1:
            resto = number % base
            lista.insert (0, resto)
            number = number // base     
        lista.insert (0, number)
        
        if base == 16:
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
###################################################################
    def all_bases_for_dec(base,number): #Qualquer base para Decimal
        lista = []
        for i in number:
            if i == "A" or i == "a":
                lista.append("10")
            elif i == "B" or i == "b":
                lista.append("11")
            elif i == "C" or i == "c":
                lista.append("12")
            elif i == "D" or i == "d":
                lista.append("13")
            elif i == "E" or i == "e":
                lista.append("14")
            elif i == "F" or i == "f":
                lista.append("15")
            else: lista.append(i)
            
        m = 1
        soma = 0
        for i in lista:
            valor = int(i)
            soma = soma + valor*base**(len(lista) - m)
            m += 1
            decimal = soma
            
        return decimal
###################################################################
#OPÇÕES:
    if option > 0 and option < 7:
        number = (input("Enter a number: "))
        print ("Resultado -> ",end="")
        if option == 1:   #Dec -> Bin
            for i in dec_for_all_bases(number,2):
                print (i, end="")
            print ("\n")
            
        elif option == 2: #Bin -> Dec
            print (all_bases_for_dec(2,number),"\n")
            
        elif option == 3: #Dec -> Hex
            for i in dec_for_all_bases(number,16):
                print (i, end="")
            print ("\n")
            
        elif option == 4: #Hex -> Dec
            print (all_bases_for_dec(16,number),"\n")
            
        elif option == 5: #Bin -> Hex
            for i in dec_for_all_bases(all_bases_for_dec(2,number),16):
                print (i, end="")
            print ("\n")
            
        elif option == 6: #Hex -> Bin
            for i in dec_for_all_bases(all_bases_for_dec(16,number),2):
                print (i, end="")
            print ("\n")

    elif option == 7:     #Others
        base = int(input("Informe a base do número que será convertido (2,3,4,5...).\nBase: "))
        number = input("Digite o número: ")
        auxiliar = all_bases_for_dec(base,number)
        
        base_nova = int(input("Informe a nova base que deseja: "))
        print ("Resultado -> ",end="")
        
        if base_nova == 10:
            print (all_bases_for_dec(base,number))
            print ("\n")
        else:
            for i in (dec_for_all_bases(all_bases_for_dec(base,number),base_nova)):
                print (i, end="")
            print ("\n")
            
    else: print ("Opção inválida!\n")
    #time sleep
    
