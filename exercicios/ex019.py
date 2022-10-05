# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido random
from random import random,randint
a1 = input('nome aluno 1 ')
a2 = input('nome aluno 2 ')
a3 = input('nome aluno 3 ')
a4 = input('nome aluno 4 ')
a = randint(1,4)
if (a == 1):
    print('{} foi escolhido(a)'.format(a1))
if(a == 2):
    print('{} foi escolhido(a)'.format(a2))
if(a == 3):
    print('{} foi ecolhido(a)'.format(a3))
if(a == 4):
    print('{} foi escolhido'.format(a4))
