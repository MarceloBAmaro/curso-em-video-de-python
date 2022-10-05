#faça um numero que leia um número qualquer e mostre seu fatorial
num = int(input('qual o numero que você quer fatorial? '))
ex = 1
for fat in range(1, num + 1):
    ex *= fat
    print(ex, end='->')
print('acabou!\n')
print('o resultado do fatorial do numero {} é {}'.format(num, ex))
