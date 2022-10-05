# crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
# depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla
from random import randint
tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print('os valores sorteados foram:', end=' ')
for h in tupla:
    print(h, end=' ')
tupla = sorted(tupla)
menor = tupla[0]
maior = tupla[len(tupla) - 1]
print('')
print(f'o menor número foi {menor}')
print(f'o maior número foi {maior}')
