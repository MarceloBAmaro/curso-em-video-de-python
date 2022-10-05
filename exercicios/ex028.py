#escreva um programa que faça o compudador "pensar" em um numero
# inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo cumputador.
# o programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
pronto = str(input('esta pronto? ')).strip().lower()
if(pronto == 'sim'):
    r = randint(0,5)
    t = str(input('qual o numero? '))
    if(t == r):
        print('você acertou, paraboins!')
    else:
        print('errou, eu pensei no numero {} tente denovo!'.format(r))
else:
    print('esfrie o cabeça e depois jogue!')

