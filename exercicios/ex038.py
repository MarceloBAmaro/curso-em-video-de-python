#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#-o primeiro valor é maior
#-o segundo valor é maior
#-não existe valor maior os dois são iguais
pv = int(input('\033[0;31;400mqual o primeiro valor? \033[m'))
sv = int(input('\033[0;31;400mqual o segundo valor? \033[m'))
if pv > sv:
    print('\033[0;36;400mo primeiro valor é maior!\033[m')
elif pv < sv:
    print('\033[0;36;400msegundo valor é maior!\033[m')
else:
    print('\033[0;36;400mos dois valores são iguais!\033[m')