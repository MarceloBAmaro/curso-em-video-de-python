#o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
from random import shuffle
a1 = str(input('qual o nome do aluno '))
a2 = str(input('qual o nome de outro aluno '))
a3 = str(input('mais um aluno '))
a4 = str(input('so mais esse '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print(lista)
#não consegui
