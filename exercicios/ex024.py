#crie um programaque leia o nome de uma cidade e diga se no nome dela começa ou nao com 'santo'
cidade = str(input('qual a sua cidade:')).lower().strip()
cidadesp = cidade.split()
cidadesp0 = cidadesp[0]
e = 'santo' in cidadesp0
print(e)
