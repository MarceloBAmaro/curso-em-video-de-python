#crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maior idade e quantas já são maiores de 18 anos.
from datetime import date
day = date.today().year
totmai = 0
totmen = 0
for pess in range(1, 8):
        nasc = int(input('em que ano a {} pessoa nasceu'.format(pess)))
        ida = day - nasc
        if ida >= 21:
            totmai += 1
        else:
            totmen += 1
print('ao todo tivemos {} pessoas maiores de idade \n e tambem tivemos {} menores de idade'.format(totmai, totmen))
#não consegui
