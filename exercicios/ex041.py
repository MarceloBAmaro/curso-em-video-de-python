#a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: sênior
#acima: mestre
from _datetime import date
day = date.today().year
nas = int(input('qual o sua data de nascimento? '))
ida = day - nas
if ida <= 9:
    print('vá para a ala dos competidores mirims!')
elif 9 < ida <= 14:
    print('vá para a ala dos competidores infantis!')
elif 14 < ida <= 19:
    print('vá para a ala dos competidores juniors!')
elif 19 < ida <= 20:
    print('vá para a ala dos campetidores senior!')
elif ida > 20:
    print('vá para a ala dos competidores mestres!')
