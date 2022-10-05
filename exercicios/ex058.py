#melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessaris para vencer
from random import randint
cont = 1
r = 0
num = randint(0, 10)
par = 0
print('\033[;36;400meu pensei em um número tente descobri-lo!\033[m')
while r != num:
    j = int(input('o número é: '))
    par += 1
    if j == num:
        r = num
        if par == 1:
            print('parabuoins de 1ª!')
        else:
            print('não fez mais do que a sua obrigação já que tentou {} vezes!'.format(par))

    else:
        print('\033[;31;400merrou!\033[m')
