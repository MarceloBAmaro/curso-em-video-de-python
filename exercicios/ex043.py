#desenvolva um programa que leia o peso e a altura de uma pessoa, e calcule se imc e mostre seu status, de acordo com a tabela abaixo.
#abaixo de 18,5:abaixo do peso
#entre 18,5 e 25:peso ideal
#de 25 a 30:sobrepeso
#de 30 a 40:obesidade
#acima de 40:obesidade morbida
alt = float(input('qual a sua altura? '))
peso = float(input('qual é o seu peso? '))
imc = peso / (alt ** 2)
print('o seu imc é de {}'.format(imc))
if(imc < 18.5):
    print('e seu status é abaixo do peso!')
elif imc > 18.5 and imc < 25:
    print('você esta no peso ideal!')
elif imc > 25 and imc < 30:
    print('seu status é sobrepeso!')
elif imc > 30 and imc < 40:
    print('seu status é obesidade!')
else:
    print('tu tá muito gordo!')