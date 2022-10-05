#crie um programa que leia  uma frase qualquer e diga se ela é um palindromo desconsiderando os espaços
frase = str(input('qual é a frase? ')).strip().lower().split()
junto = ''.join(frase)
inverso = junto[::-1]
if junto == inverso:
    print('tu tens um palíndromo!')
else:
    print('tu não tens um palíndromo!')
#não consegui

