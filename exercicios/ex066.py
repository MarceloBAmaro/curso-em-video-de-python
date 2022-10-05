# crei um programa que leia vrios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999, que é acondição de parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)
cont = soma = 0
while True:
    resp = int(input('qual é o numero? '))
    if resp == 999:
        break
    print('\033[;31;400mERROU\033[m')
    cont += 1
    soma += resp
print(f'\033[;32;400mACERTOU\033[m\ngastou {cont} numeros e a soma deles é {soma}')


