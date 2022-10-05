# crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. no final mostre quantos numeros foram digitados e qual foi a soma entre eles
# desconsiderando o flag
a = 0
cont = 0
soma = 0
while a != 10:
    num = int(input('qual a senha? '))
    soma = soma + num
    if num != 999:
        a -= 1
        print('\033[;31;400mERROU\033[m')
    elif num == 999:
        a = 9
    cont += 1
    a += 1
print('\033[;32;400mpabens você acertou!\033[m \nvocê digitou {} numeros e a soma entre eles é {}'.format(cont - 1, soma - 999))
