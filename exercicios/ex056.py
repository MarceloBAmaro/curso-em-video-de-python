#desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. no final mostre:
#a média de idade do grupo
#qual o nome do homen mais velho
#quantas mulheres tem menos de 20 anos
from datetime import date
day = date.today().year
somida = 0
idaa = 0
homenv = ''
qnovinha = 0
for grupo in range(1, 5):
    print('\033[;36;400m=\033[m' * 20, '\033[;36;400m{}ª pessoa\033[m'.format(grupo), '\033[;36;400m=\033[m' * 20)
    nome = str(input('qual o nome da {}ª pessoa?      |'.format(grupo)))
    nasc = int(input('em que ano a {}ª pessoa nasceu? |'.format(grupo)))
    sexo = str(input('qual o sexo da {}ª pesoa?       |'.strip().format(grupo)))

    ida = day - nasc
    somida += ida

    if nome == 'masculino':
        if ida >= idaa:
            idaa = ida
            homenv = nome
        if sexo == 'feminino' and ida > 20:
            qnovinha += 1
média = somida / 4
print('\033[;31;400m=\033[m' * 51)
print('a pessoa mais velha é {}!'.format(homenv))
print('a idade média do grupo é {:.2f} anos!'.format(média))
print('há {} mulheres com menos de 20 anos nesse grupo!'.format(qnovinha))
