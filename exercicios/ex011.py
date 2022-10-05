#faça um programa que leia a largura e a altura de uma
# parede em metros,calcule a sua area e a quantidade de tinta
# necessaria para pinta-la, sabendo que cada litro de tinta pinta
# uma area de 2m
l = float(input('digite a largura '))
a = float(input('digite a altura '))
área = l*a
t = 2
print('a área é {}M e se precisa de {}l para pintala'.format(área,área/t))