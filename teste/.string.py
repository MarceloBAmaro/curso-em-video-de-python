#foelldizz
frase = str(input('digite a senha '))
print(frase[::2])#vai printar a frase entre os espaçamentos desejados
c = len(frase)#conta o numero de caracteres em uma string
print(c)
n = frase.count('l',0,4)#conta o numero de letras de uma letra desejada
print(n)
a = frase.find('amo')#procura no texto uma frase ou uma letra e indica sua posiçao em numeros
print(a)
e = 'sii' in frase#avalia se tem tal palavra ou letra no texto
print(e)
r = frase.replace('o','a')#procura uma letra ou palavra e a substiui por outra desejada
print(r)
M = frase.upper()#deixa todas as letras em maiusculo
print(M)
m = frase.lower()#deixa todas as letras em minusculo
print(m)
z = frase.capitalize()#deixa só o primeira letra da primeira palavra maiuscula
print(z)
t = frase.title()#deixa todas as primeiras letras em maiuscula
print(t)
s = frase.strip()#excluir todos os espaços inuteis
print(s)
rs = frase.rstrip()#exclui todos os espaços inuteis mais somente o direita
print(rs)
ls = frase.lstrip()#exclui todos os espaços inuteis mais somente a direita
print(ls)
sp = frase.split()#cria ma divisão onde ha espaço
print(sp)
j = ''.join(frase)#juntar frases que foram splitados
print(j)
sp0 = sp[0][1]
print(sp0)