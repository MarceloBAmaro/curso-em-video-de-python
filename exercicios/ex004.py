#faça um programa que leia algo pelo tevlado e mostre
#na tela o seu tipo primitivo e todas as informaçoes possiveis sobre ela
algo = input('\033[7;35;41mdigite algo\033[m')
print(algo.isalnum())
print(algo.isalpha())
print(algo.isupper())
print(algo.isdecimal())
print(algo.isnumeric())
