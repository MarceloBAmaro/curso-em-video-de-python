# crie um progama que leia a idade  e o sexo de varias pessoas. a cada pessoa cadastrada o programa deverá perguntar se o usuario quer ou não continuar. no final, mostre :
# A quantas pessoas tem mais de 18 anos
# B quantos homens foram cadastrados
# C quantes mulheres tem menos de 20 anos
cont18 = contH = contM20 = 0
while True:
    sexo = str(input('seu sexo: ')).strip()[0]
    ida = int(input('sua idade: '))
    if ida >= 18:
        cont18 += 1
    if sexo in 'Mm':
        contH += 1
    if sexo in 'Ff' and ida < 20:
        contM20 += 1
    if sexo not in 'MmFf':
        print('\033[;31;400m=\033[m' * 21)
        print('ação nao possivel!')
        print('\033[;31;400m=\033[m' * 21)
    print(sexo)
    print(contH)
    esc = str(input('deseja continuar?:'))
    print('\033[;36;400m=\033[m' * 21)
    if esc[0] in 'Nn':
        print(f'{cont18} maiores de 18 anos foram cadastrados\n{contH} homens foram cadastrados\n{contM20} mulheres tem menos de 20 anos')
        print('\033[;37;400m=\033[m' * 21)
        print('sistema desligado')
        break
