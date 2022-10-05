#desenvolva m prograa que pergunta a distancia de uma viagem em km.
#calcule o preço da passagem, cobrando R$0,50 por km para viagems de até 200km e R$0,45 para viagens mais longas.
dis = float(input('qual a distancia em KM? '))
if(dis < 200):
    print('você pagara {} reais em sua viagem'.format(dis * 0.5))
else:
    print('você pagara {} rais em sua viagem'.format(dis * 0.45))