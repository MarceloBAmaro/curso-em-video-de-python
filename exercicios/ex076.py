# crie um programa que tenha uma tupla únicacom nomes de produtos e seus respectivos preços, nasequencia
# no final, mostre uma listagem de preços, organizando os dados em forma tabular
# lista = (str(input('qual o 1º produto?: ')), int(input('qual o preço do 1º produto?: ')), str(input('qual o 2º produto?: ')), int(input('qual o preço do 2º produto?: ')), str(input('qual o 3º produto?: ')), int(input('qual o preço do 3º produto?: ')), str(input('qual o 4º produto?: ')), int(input('qual o preço do 4º produto?: ')), str(input('qual o 5º produto?: ')), int(input('qual o preço do 5º produto?: ')), str(input('qual o 6º produto?: ')), int(input('qual o preço do 6º produto?: ')), str(input('qual o 7º produto?: ')), int(input('qual o preço do 7º produto?: ')), str(input('qual o 8º produto?: ')), int(input('qual o preço do 8º produto?: ')), str(input('qual o 9º produto?: ')), int(input('qual o preço do 9º produto?: ')), str(input('qual o 10º produto?: ')), int(input('qual o preço do 10º produto?: ')))
braco = 0
lista = ('lapis', 1.75, 'borracha', 2, 'caderno', 15.90, 'estojo', 25, 'transferidor', 4.20, 'compasso', 9.99, 'mochila'
         , 120.32, 'canetas', 22.30, 'livro', 34.90)
print('\033[1;36;400m_\033[m' * 30)
print('\033[1;36;400m{:_^30}\033[m'.format('tabela dos preços'))
print('')
for cont in range(0, 9):
    print('{:-<21}R${:>7.2f}'.format(lista[braco], lista[braco + 1]))
    braco += 2
print('\033[1;36;400m_\033[m' * 30)

