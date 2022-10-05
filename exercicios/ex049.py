# faça o desafio 009, mostrando a tabuada de um numero que o o usuario escolher, só que agora utilizando o laço for.
num = float(input('qual o numero? '))
for tab in range(0, 11):
    mut = num * tab
    print(mut, end='\n')
