print('*' *30)
print('Analisador de triângulos')
print('*' * 30)
r1 = float(input('Comprimento da primeira reta'))
r2 = float(input('Comprimento da segunda reta'))
r3 = float(input('Comprimento da terceira reta'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Estas retas podem formar um triângulo')
else:
    print('Estas retas não podem formar um triângulo')
