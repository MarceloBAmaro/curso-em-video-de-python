#faça um algoritimo que leia o salario de um funcionario e
#mostre seu novo salario, com 15% de aumento

sa = float(input('qual seu salario antigo '))
sn = sa+(sa/6.666666666666667)
print('seu salario antigo era {}$R e agora é {}$R'.format(sa,sn))