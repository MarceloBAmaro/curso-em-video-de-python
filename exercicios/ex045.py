# crie um programa que faça o computador jogar jokenpô com você
from time import sleep
from random import choice

sim = str(input('vamos jogar jokenpô? ')).strip().lower()
if sim == 'sim':
    sue = str(input('qual a sua escolha? '))
    l = ['tesoura', 'pedra', 'papel']
    coe = choice(l)
    a = print('jo', end=''), sleep(1), print('-ken', end=''), sleep(1), print('-pô'), sleep(0.5)
    print(coe)
    if sue == 'tesoura' and coe == 'pedra':
        print('você perdeu ')
    elif sue == 'pedra' and coe == 'papel':
        print('você perdeu')
    elif sue == 'papel' and coe == 'tesoura':
        print('você perdeu')
    elif sue == coe:
        print('empate, não ouve ganhador')
    else:
        print('você ganhou, paraboins')
else:
    print('pode jogar outra hora ')
