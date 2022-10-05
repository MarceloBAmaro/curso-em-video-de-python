#faça um programa que leia três numeros e mostre qual o maior e qual é o menor
n1 = float(input('qual o primeiro numero? '))
n2 = float(input('qual o segundo numero? '))
n3 = float(input('qual o terceiro numero? '))
#verifica quem é o maior
if(n1 > n2) and (n1 > n3):
    print('o maior numero é {}'.format(n1))
if(n2 > n1) and (n2 > n3):
    print('o maior numero é {}'.format(n2))
if(n3 > n1) and (n3 > n2):
    print('o maior numero é {}'.format(n3))
#verifica quem é o menor
if(n1 < n2) and (n1 < n3):
    print('o menor numero é {}'.format(n1))
if(n2 < n1) and (n2 < n3):
    print('o menor numero é {}'.format(n2))
if(n3 < n2) and (n3 < n1):
    print('o menor numero é {}'.format(n3))

