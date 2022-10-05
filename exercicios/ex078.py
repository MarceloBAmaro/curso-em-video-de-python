# faça um programa que leia 5 valores e guarde-os em uma lista.
# no final mostre qual foi o maior valor e o menor valor e as suas respectivas posições na lista
lista = posm = posM = list()
for c in range(0, 5):
    valor = input(f'qual o valor na posição {c}?: '.strip())
    lista.append(valor)
    if c == 0:
        maiorv = valor
        menorv = valor
        posm.append(c)
        posM.append(c)
    elif maiorv < valor:
        maiorv = valor
        #if
        #posM.append(c)
        #del posM[0]
    elif menorv > valor:
        menorv = valor
        posm = c
lista.sort()
print('=' * 28)
print(f'o menor valor da lista é: {lista[0]} na posição {posm}')
print(f'o maior valor da lista é: {lista[-1]} na posição {posM}')
