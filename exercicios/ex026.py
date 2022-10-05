#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra "a"
#em que posiçao ela aparece a primeira vez
#em que posiçao ela aperece a ultima vez
frase = str(input('digite o texto: ')).strip().lower()
ff = frase.find('a')+1
fc = frase.count('a')
fcu = frase.rfind('a')+1
print(ff)
print(fc)
print(fcu)
#não consegui
