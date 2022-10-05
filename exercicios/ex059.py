#crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos numeros
#[5]sair do programa
#seu programa deverá realizar a operação solicitada em cada caso.
j = 0
num1 = float(input('qual o primeiro numero? '))
num2 = float(input('qual o segundo numero? '))
while j != 5:
    print('\033[;36;400m=+=\033[m' * 20)
    print('[1]somar\n[2]mutiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa')
    esc = int(input('qual a sua escolha? '))
    if esc == 1:
        print('o resultado da soma é {}'.format(num1 + num2))
    elif esc == 2:
        print('o resultado da mutiplicação e {}'.format(num1 * num2))
    elif esc == 3:
        if num1 > num2:
            print('o numero {} é maior!'.format(num1))
        elif num1 < num2:
            print('o numero {} é maior!'.format(num2))
        elif num1 == num2:
            print('os dois valores são iguais!')
        else:
            print('a operação não pode ser realizada!')
    elif esc == 4:
        num1 = float(input('qual o novo primeiro número? '))
        num2 = float(input('qual o novo segundo número '))
    elif esc == 5:
        print('o sistema foi desligado!')
        j = 5
    elif esc == 2009:
        print('parabens você descobriu a data do meu nascimento e isso que dizer que ou você é um haker ou tem muita sorte!')
    else:
        print('operação impossivel!')
