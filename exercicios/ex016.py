#crie um programa que leia um numero real qualquer e mostre na tela sua porçao inteira
from math import floor
num = float(input('digite um numero '))
pi = int(floor(num))
print('o numero é {} e sua porção inteira é {}'.format(num,pi))