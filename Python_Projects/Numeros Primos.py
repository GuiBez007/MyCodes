#FUNÇÃO DE CÁLCULO PARA NÚMEROS PRIMOS
def is_prime(num):
    if num % 2 == 0: #elimina números pares
        if num == 2: #(com exceção do 2)
            return True
        else: return False
    
    for a in range (1, num+1):
        if a == 1 and num % 1 == 0:
            continue
        elif num % a == 0 and num != a:
            return False
    return True


x = int(input('Quero números primos de 1 até '))
for i in range(1, x): #encontrar números primos de 1 a x
    if is_prime(i + 1): #se PRIMO...
        print(i + 1, end=" ") #mostra na tela

input()
