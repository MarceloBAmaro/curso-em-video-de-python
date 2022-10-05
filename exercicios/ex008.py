#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m = int(input('\033[4;30;41mquantos metros\033[m'))
c = m*100
ml = m*1000
print('\033[4;30;41mem centimetros {} em milimetros {}\033[m'.format(c,ml))
