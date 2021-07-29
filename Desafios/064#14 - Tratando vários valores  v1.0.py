num = cont = total = 0
while num != 999:
    if num != 999:
       num = int(input('Digite um número [999 para parar]:'))
       total += num
       cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont -1 ,total - 999))
#solução do professor
'''num = cont = total = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    total += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,total))'''
