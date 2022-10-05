# faça um programa que calcule a soma de todos os numeros impares que sao mutiplos de 3 e que se incontram no intervalo de 1 até 500
som = 0
for inp in range(1, 500, 2):
    if inp % 3 == 0:
        som = inp + som
print(som)
