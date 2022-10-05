# crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte oa usuario qual será o valor sacado(numero inteiro) e o programa vai informar quantas cedulas de cada valor serao intregues
# considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.
valor = int(input('qual o valor?: R$'))
tot = valor
céd = 50
totcéd = 0
while True:
    if tot >= céd:
        tot -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'são {totcéd} cedulas de R${céd:.2f}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if tot == 0:
            break
# não consegui

