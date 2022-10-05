#elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condiçao de pagamento
#a vista dinheiro/cheque:10% de desconto
#a vista no cartão:5% de desconto
#em até 2X no cartão:preço normal
#3X ou mais no cartão:20% de juros
preço = float(input('qual o preço? '))
forp = input('qual a forma de pagamento? ').strip().lower()
if forp == 'cartão' or forp == 'cartao':
    parc = int(input('em quantas parcelas? '))
    if parc > 2:
        print('o preço é {} reais e cada parcela fica por {:.2f} reais!'.format(preço + preço * 20 / 100,  (preço + (preço * 20 / 100))/parc))
    elif parc == 2:
        print('o preço é {} reais e cada parcela fica por {} reais!'.format(preço,preço / 2))
    else:
        print('o preço é {} reais!'.format(preço))
elif forp == 'cheque':
    print('o preço é {} reais com um desconto\n de 10% o preço fica por {} reais!'.format(preço,preço - preço * 10 / 100))
elif forp == 'dinheiro':
    print('o preço é {} reais com um desconto\n de 10% o preço fica por {} reais!'.format(preço,preço - preço * 10 / 100))
else:
    print('não aceitamos esse tipo de pagamento!')