# escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80KM/h, mostre uma mensagem dizendo que ele foi multado.
# a multa vai custar R$7,00 por cada KM acima do limite
vc = int(input('qual a velocidade do carro? '))
if (vc > 80):
    if (vc == 0):
        print('você foi multado em um valor de {} reais por estar a {} km/h'.format(vc + 7, vc))
    else:
        print('você foi multado em um valor de {} reais por estar a {} km/h'.format((vc - 80) * 7,vc))
else:
    print('pode prosseguir, tenha uma boa viagem!')
