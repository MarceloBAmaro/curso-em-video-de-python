#crie um programa que leia um numero inteiro e mostre na tela se ele é par om inpar
import math
num = int(input('qual o numero? '))
v = num % 2
if(v == 0):
    print('é par')
else:
    print('é inpar')