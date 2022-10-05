# escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual a base de conversão.
# para binario
# para octogonal
# para exadecimal
print('\033[0;36;400m1-binario\n2-octogonal\n3-exadecimal\033[m')
escolha = int(input('qual a escala de converersão 1 2 ou 3? '))
num = int(input('qual numero? '))
if escolha == 1:
    print('em binario o nuero fica {}'.format(bin(num)[2:]))
elif escolha == 2:
    print('em octo fica {}'.format(oct(num)[2:]))
elif escolha == 3:
    print('em exadecimal fica {}'.format(hex(num)[2:]))
else:
    print('não existe a opção {}'.format(escolha))
#não consegui