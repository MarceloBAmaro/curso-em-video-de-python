#refaça o desafio 035 dos triangulos, acrecentando  o recurso de mostrar qual triangulo sera formado
r1 = float(input('qual a primeira reta? '))
r2 = float(input('qual a seguda reta? '))
r3 = float(input('qual a terceira reta? '))
if r1 + r2 < r3 or r1 + r3 < r2 or r2 + r3 < r1:
    print('você não tem um triangulo!')
else:
    print('você tem um triangulo!')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('você tem um triangulo do tipo equilatero!')
    elif r1 == r2 and r1 == r3:
        print('você tem um triangulo do tipo isoceles!')
    else:
        print('você tem um triangulo do tipo escaleno!')