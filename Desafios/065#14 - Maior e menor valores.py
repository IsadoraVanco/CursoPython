contagem = maior = menor = total = 0
af = 's'
num = 0
while af != 'N':
    num = int(input('Qual será o número?'))
    contagem += 1
    total += num
    if contagem == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        elif num > maior:
            maior = num
    af = str(input('Quer continuar? [S/N]')).strip().upper()
media = total / contagem
print('Você digitou {} números e a média foi {:.2f}'.format(contagem,media))
print('O maior valor foi de {} e o menor foi {}'.format(maior, menor))



