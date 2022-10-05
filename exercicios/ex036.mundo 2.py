#escreva um programa para aprovar o emprestimo bancario de uma casa. o programa vai perguntar o nome da casa, o salario do comprador e em quantos anos ele vai pagar.
#calcule o valor da pestação mensal sabendo que ela não pode exeder 30% do salario ou entao o emprestimo sera negado
vc = float(input('qual o valor da casa? '))
ss = float(input('qual é o seu salario? '))
qa = int(input('em quantos anos pretende pagar o emprestimo? '))
qm = qa * 12
a = vc / qm
pds = ss * 30 / 100
if(a > ss * 30 / 100):
    print('\033[4;31;400mseu pedido foi negado!\033[m')
else:
    print('\033[0;32;400mseu pedido foi aprovado passara por 3999 agencias e você recebera \nseu dinheiro daqui 1000 anos. brasil né pai\033[m')
print(a)
print(ss * 30 / 100)