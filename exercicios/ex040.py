#crie um program que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem final, de acordo com a media atingida
#reprovado = média abaixo de 5.0
#recuperação = média  de 5.0 a 6.9
#aprovado = média acima de 7.0
n1 = float(input('qual a sua primeira nota? '))
n2 = float(input('qual a sua segunda nota? '))
média = (n1 + n2) / 2
if média < 5.0:
    print('\033[1;31;400mreprovado\033[m')
elif média > 5.0 and média < 7:
    print('recuperação')
else:
    print('\033[0;32;400maprovado\033[m')
