#crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas a letras maiusculas
#o nome com todas as letras minusculas
#quantas letras ao todo sem considerar espaço
#quantas letras tem o primeiro nome
nome = str(input('qual seu nome completo: '))
nomeM = nome.upper()
print(nomeM)
nomem = nome.lower()
print(nomem)
nometl = len(nome) - nome.count(' ')
print(nometl)
nomesp = nome.split()
nomespc = len(nomesp[0])
print(nomespc)
#não consegui

