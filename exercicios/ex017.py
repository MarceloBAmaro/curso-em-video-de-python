#faça um programa que leia o cromprimento do cateto oposto
#e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
a = float(input('cateto a '))
b = float(input('cateto b '))
s = (b**2) + (a**2)
c = pow(s,1/2)
print('o cateto a é {} o cateto b é {} e a hipotenusa c é {}'.format(a,b,c))