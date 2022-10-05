#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dollares ela pode comprar
#1 dollar = 3,27 reais
n = float(input('quanto quer converter '))
d = 3.27
print('você recebeu {:.2f} dollares e gastou {} reais'.format((n/d),n))
