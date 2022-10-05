# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# seu programa deverá ler um numero pelo teclado(entre 0 e 20)e mostra-lo por extenso
# desafio: faça seu programa pergutar se o usuari quer continuar
cont = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
númex = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print('\033[0;36;400m{:=^53}\033[m'.format('contagem'))
for conam in cont:
    print(conam, end=' ')
print('')
print('\033[0;36;400m=\033[m' * 53)
print('\033[0;31;400m=\033[m' * 53)
while True:
    núm = int(input('qual o número?: '))
    if núm > len(cont) or núm < 0:
        print('\033[1;31;400mERRO\033[m tente novamente')
    else:
        pos = cont.index(núm)
        print(f'\033[;;40mo numero é \033[m\033[;31;40m{númex[pos]}\033[m')
        resp = str(input('quer continuar?:'))
        print('=' * 53)
        if resp[0] in 'Nn':
            break

