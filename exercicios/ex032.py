#faça um programa que leia um ano e mostre se ele é bissexto
ano = int(input('qual o ano? '))
anop4 = ano % 4
if(anop4 == 0):
    print('o ano é bissexto!')
else:
    print('o ano não ébissexto!')