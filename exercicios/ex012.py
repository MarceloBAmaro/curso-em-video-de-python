#faça um algoritimo que leia opreço de um produto e mostre seu novo preço com 5% de desconto
po = float(input('qual o preço original '))
pd = po-(po/20)
print('o preço original é {}$R e com o desconto é {}$R'.format(po,pd))
