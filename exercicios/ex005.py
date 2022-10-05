# faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input('\033[1;33;45mdigite um numero \033[m'))
print('\033[4;31;45mseu antecessor é {} e seu sucessor é {}\033[m'.format(numero - 1, numero + 1))
