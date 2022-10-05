from time import sleep
print('\033[1;36;400mcole ou escreva seus nomes a serem contados com espaços entre cada um!\033[m')
sleep(1)
nomes = str(input('quai são os nomes? ')).split()
print('são {} nomes!'.format(len(nomes)))


