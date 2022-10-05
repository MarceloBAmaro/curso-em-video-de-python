#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade.
#-se ele ainda vai se alistar no exercito
#-se é a hora de ele se alistar
#seu programa tambem deverá mostrar o tempo que falta ou que passou o prazo
from _datetime import date
day = date.today().year
#day = int(input('insira o ano atual! '))
nas = int(input('qual seu ano de nascimento? '))
if 18 == day - nas:
    print('é hora de se alistar!')
elif 18 > day - nas:
    print('daqui a pouco sera sua hora de servir a patria!')
elif day - nas == 17:
    print('faltam {} anos para você servir!'.format(((day - nas) - 18)*-1))
elif day - nas > 18:
    print('já passou a hora de se alistar!')

