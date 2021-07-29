s = 0
c = 0
for numeros in range(1,501,2):
    if numeros % 3 == 0:
        s = s + numeros
        c +=1
print('A soma de todos os {} valores solicitados é {}'.format(c,s))
