#faça um programa que leia o peso de cinco pessoas. no final mostre qual foi o maior peso e qual foi o menor peso
maior = 0
menor = 0
for pes in range(1, 6):
    peso = float(input('qual o peso da {}ª pessoa: '.format(pes)))
    if pes == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('\033[;36;400m=+=\033[m'*9)
print('o maior peso foi {}KG \ne o menor peso foi {}KG'.format(maior, menor))
#não consegui
