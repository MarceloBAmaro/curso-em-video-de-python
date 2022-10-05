#faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "m" ou "f". caso esteja errado, peça a digitação novemente até ter um valor correto.
from time import sleep
n = 1
while n != 0:
    n = str(input('qual seu sexo? ')).lower().strip()
    if n == 'm' or n == 'f':
        n = 0
    else:
        n = 1
        print('\033[;31;400mdigite novamente!\033[m')
        sleep(1)
print('seu sexo foi aceito pela sociedade!')
