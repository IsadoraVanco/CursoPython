#maneira mais fácil de fazer

'''cat1 = float(input('Comprimento do cateto oposto'))
cat2 = float(input('Comprimento do cateto adjacente'))
hip = (cat1**2+cat2**2) ** (1/2)
print('O comprimento da hipotenusa será de {:.2f}'.format(hip))'''

#Maneira usando módulos
from math import hypot
cat1 = float(input('Comprimento do cateto oposto'))
cat2 = float(input('Comprimento do cateto adjacente'))
hip = hypot(cat1, cat2)
print('A hipotenusa vai medir {:.2f}'.format(hip))



