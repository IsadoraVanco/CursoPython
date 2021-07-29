r1 = float(input('Comprimento da primeira reta:'))
r2 = float(input('Comprimento da segunda reta:'))
r3 = float(input('Comprimento da terceira reta:'))
if r1==r2 and r2==r3 and r3==r1:
    print('Estas retas podem formar um triângulo EQUILÁTERO.')
elif r1==r2 or r2==r3 or r3==r1:
    print('Estas retas podem formar um triângulo ISÓSCELES.')
else:
    print('Estas retas podem formar um triângulo ESCALENO.')
