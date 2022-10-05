#escreva um programa que pargunta a quantidade de
# km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. calcula o preço
# a pagar, sabendo que o carro custa R$6o por dia e R$0,15 por km rodado
km = float(input('quantos km você rodou '))
dia = int(input('alugou por quantos dias '))
pkm = km*0.15
pdia = dia*60
total = pkm+pdia
print('o tota que você tem a pagar é {}R$'.format(total))