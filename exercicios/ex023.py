#faça um programa qie leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
numero = int(input('digite um numero de 4 digitos: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(m)
print(c)
print(d)
print(u)
#não consegui