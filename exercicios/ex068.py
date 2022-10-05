# faça um programa que jogue par ou inpar com o computador. o jogo só sera interrompid se o jogador vencer, mostrando o total de vitorias consecutivas que ele conquistou ao final do jogo
from random import randint
cont = 0
while True:
    escc = randint(0, 10)
    esc = str(input('qual a sua escolha? ')).strip().lower()
    escn = int(input('qual o numero? '))
    if esc == 'par' and (escc + escn) % 2 == 0:
        print('você ganhou!')
        cont += 1
    elif esc == 'impar' and (escc + escn) % 2 == 1:
        print('você ganhou')
        cont += 1
    else:
        print(f'você perdeu com {cont} vitorias consecutivas!')
        break
