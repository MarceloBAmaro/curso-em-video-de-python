#melhore o desafio 061, perguntando para o usuario se ele quer mais alguns termos. o programa encerra quando ele disser que quer mostrar 0 termos.
termo = int(input('qual o termo inicial? '))
razão = int(input('qual a razão? '))
a = 1
macaco = termo
q = 11
while a != q:
    if a == 1:
        print(f'{termo}|', end='')
    else:
        print(f'{macaco}|', end='')
    macaco += razão
    a += 1
    if a == q:
        termom = int(input('\nquantos termos você quer a mais? '))
        if termom == 0:
           print('')
        else:
            q += termom
