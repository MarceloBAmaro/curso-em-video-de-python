# crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato de futbol, na ordem de colocação. depois moste:
# A apenas os 5 primeiros colocados
# B os ultimos quatro colocados da tabela
# C uma lista com os times e ordem alfabetica
# D em que posição esta o time da chapecoense
cont = 0
times = (
    'palmeiras', 'flamengo', 'corinthians', 'internacional', 'fluminense', 'athletico-pr', 'atletico-mg', 'america-mg',
    'goias', 'santos', 'bragantino', 'fortaleza', 'botafogo', 'são paulo', 'ceara sc', 'cuiaba', 'coritiba', 'avai',
    'atletico-go', 'juventude')
print('\033[1;32;400m{:=^107}\033[m'.format(' times do brasileirão '))
for p in times:
    if cont == 9:
        print('')
    else:
        print(f'\033[0;34;400m{p}\033[m', end=', ')
    cont += 1
print('\033[0;34;400mfinal.\033[m')
print('os 5 primeiros times do brasileirão são:')
for b in times[:5]:
    print(f'\033[;31;400m{b}\033[m')
print('os 4 piores times do brasileiãro são:')
print(f'\033[;31;400m{times[-4]}\033[m')
print(f'\033[;31;400m{times[-3]}\033[m')
print(f'\033[;31;400m{times[-2]}\033[m')
print(f'\033[;31;400m{times[-1]}\033[m')
print('em ordem alfabetica os times se organizam assim:')
cont = 0
for a in sorted(times):
    if cont == 9:
        print('')
    else:
        print(f'\033[0;34;400m{a}\033[m', end=', ')
    cont += 1
print('')
print('\033[;33;400ma chapecoense atualmente esta na 14ª posição do brasileião serie B\033[m')
