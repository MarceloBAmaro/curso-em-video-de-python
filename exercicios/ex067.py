# faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valos digitado pelo usuario. o programa será interrompido quando o numero solicitado for negativo
cont = 0
from time import sleep

while True:
    num = int(input('\033[;36;400mqual o valor? \033[m'))
    cont += 1
    if num < 0:
        print('sistema desligado!')
        break
    while cont != 11:
        print(f'{num} x {cont} = \033[;31;400m{num * cont}\033[m')
        sleep(0.35)
        cont += 1
    cont = 0
