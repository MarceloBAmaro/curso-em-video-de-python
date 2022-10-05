#crie um programa que leia varios numeros inteiros pelo teclado. no final mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. o prograa deve perguntar se ele quer ou nao continuar a digitar os valores ou não
a = 0
cont = 0
soma = 0
while a != 2:
    cont += 1
    num = int(input('qual é o valor? '))
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
    esc = str(input('\033[;36;400mvocê quer parar de digitar?\033[m ')).strip().lower()
    if esc == 'sim':
        a = 2
    else:
        a -= 1
média = soma / cont
print('a média entre todos os valores é {}\no maior valor é {} e o menor é {}'.format(média, maior, menor))
