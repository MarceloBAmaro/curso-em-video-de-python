#desenvolva um programa que leia o primeiro termo e a razão de uma pa. no final, mostre os 10 primeiros termos dessa progreção
prit = int(input('qual o termo? '))
raz = int(input('qual a razão? '))
if raz == 10:
    final = raz
else:
    final = raz * 10
if final == 10 and raz == 10:
    print('impossivel realizar ação')
else:
    for p in range(prit, final, raz):
        print(p)
