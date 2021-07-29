f = str(input('Digite uma frase:')).upper().strip().split()
j = ''.join(f)
i = ''
for c in range(len(j) -1, -1, -1):
     i += j[c]
print('O inverso de {} é {}'.format(j,i))
if j == i:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')

#outra maneira que poderia resolver este problema
'''f = str(input('Digite uma frase:')).upper().strip().split()
j = ''.join(f)
i = j[::-1]
print('O inverso de {} é {}'.format(j,i))
if j == i:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')'''



