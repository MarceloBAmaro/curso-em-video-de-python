#desenvolva um programa que leia 6 numeros inteiros e mostre a soma somente daqueles valores que forem pares, se o valor for impar desconsidere-o
o = 0
for opç in range(0, 6):
    num = int(input('qual o numero? '))
    if num % 2 == 0:
        o += num
print(o)

