# refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressão usando a strurura while.
termo = int(input('qual o termo? '))
razão = int(input('qual a razão? '))
a = 1
b = termo
while a != 11:
    a += 1
    if a < 11:
        print(f'{b}->', end='')
    else:
        print(b)
    if a == 11:
        print('\ncom o termo {} e a razão {} temos essa progreção aritimetica'.format(termo, razão))
    b += razão
