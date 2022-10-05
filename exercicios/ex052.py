# faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo
num = int(input('qual o numero? '))
a = 1
b = 0
for l in range(1, num + 1):
    if num % l == 0:
        b += 1
if b == 2:
    print('o numero é primo!')
else:
    print('o numero não é primo!')
