# crie um programa que leia o nome e o preço de varios produtos. o programa deverá perguntar se o usuario vai continuar. no final, mostre
# A qual é o total gasto na compra
# B quantos produtos costam mais de R$ 1000
# C qual é o nome do produto mais barato
cont = total = pre1000 = 0

while True:
    cont += 1
    nome = str(input('qual o nome?:'))
    preço = float(input('qual o preço?:'))

    if cont == 1:
        nomebara = nome
        prebara = preço
    else:
        if preço < prebara:
            nomebara = nome
            prebara = preço
    if preço > 1000:
        pre1000 += 1
    if preço > 10000:
        print('tens money pra caramba')
    esc = str(input('quer continuar?:'))
    print('\033[;36;400m=\033[m' * 37)
    total += preço
    if esc[0] in 'Nn':
        print(f'o total gasto na compra é R${total:.2f}\nna compra há {pre1000} produtos acima de R$1000\no nome do produto mais barato é \033[;;42m {nomebara} \033[m')
        break