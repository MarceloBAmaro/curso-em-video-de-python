# desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre
# A quantas vezes apareceu o numero 9
# B em que posição foi digitado o prmeiro valor 3
# C quais foram os numeros pares
tupla = (int(input('qual o primeiro valor?:')), int(input('qual o segundo valor?:')), int(input('qual o terceiro valor?:')), int(input('qual o quarto valor?:')))
if tupla[0] < 0 or tupla[1] < 0 or tupla[2] < 0 or tupla[3] < 0:
    print('\033[1;31;400mERRO\033[m reinicie o sistema!')

else:
    if tupla[0] > 8000 or tupla[1] > 8000 or tupla[2] > 8000 or tupla[3] > 8000:
        print('\033[;31;400mé mais de oito mil\033[m')
    print('\033[1;36;400m{:#^50}\033[m'.format(' resultados '))
    print(f'o número 9 apareceu {tupla.count(9)} vezes')
    if tupla.count(3) == 0:
        print('não há 3 nos valores digitados')
    else:
        print(f'o primeiro valor 3 foi digitado na posição {tupla.index(3) + 1}')
    for cont in range(0, 4):
        if tupla[cont] % 2 == 0:
            print(f'o {cont + 1}º valor é \033[0;32;400mPAR\033[m')
        elif tupla[cont] % 2 != 0:
            print(f'o {cont + 1}º valor é \033[0;33;400mIMPAR\033[m')
