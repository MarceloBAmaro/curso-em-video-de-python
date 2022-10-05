#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nome = str(input('qual e seu nome completo ')).strip()
nomesp = nome.split()
print(nomesp[0])
print(nomesp[len(nomesp)-1])
#não consegui