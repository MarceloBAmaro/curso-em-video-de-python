# crie um programa que tenha uma tupla com varias palavras(não usar acentos). depoi disso, você deve mostrar, para cada palavra, quais são sauas vogais
lista = ('imflamar', 'ornitorrinco', 'botanico', 'coiote', 'roleta', 'disciplina', 'mapa-do-mundo', 'loja', 'assalto',
         'mosquito', input('qual palavra quer adicionar? '))
for cont, pala in enumerate(lista):
    cont = 0
    while True:
        if pala[cont] not in "aeiou":
            print(pala[cont], end="")
        else:
            print(f"\033[0;32;400m{pala[cont]}\033[m", end="")
        cont += 1
        if cont == len(pala):
            print(end=" \033[0;36;400m|\033[m ")
            break
    cont = 0
    while True:
        if "a" in pala[cont]:
            print('\033[0;32;400ma\033[m', end=" ")
        elif "e" in pala[cont]:
            print('\033[0;32;400me\033[m', end=" ")
        elif "i" in pala[cont]:
            print('\033[0;32;400mi\033[m', end=" ")
        elif "o" in pala[cont]:
            print('\033[0;32;400mo\033[m', end=" ")
        elif "u" in pala[cont]:
            print('\033[0;32;400mu\033[m', end=" ")
        cont += 1
        if cont == len(pala):
            break
    print('')
    print('\033[1;36;400m=\033[m' * 30)