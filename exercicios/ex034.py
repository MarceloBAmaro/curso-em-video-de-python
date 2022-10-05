#escreva um programa que pergunte o salario de um fumsionario e calcule o valor de seu almento.
#para salarios superiores a R$1.250.00,calcule um aumeto de 10%.
#para os inferiores ou iguais calcule um almento de 15%
sal = float(input('qual seu salario? '))
if(sal > 1250):
    print('seu salario novo é de {:.2f} reais'.format(sal + sal * 10 / 100))
else:
    print('seu salario vo é de {:.2f} reais'.format(sal + sal * 15 / 100))
