print('-*' * 20)
print('CAIXA ELETRÔNICO')
print('-*' * 20)
valor = int(input('Qual o valor a ser sacado?R$'))
cinq = vinte = dez = um = 0
while True:
    while valor >= 50:
        valor = valor - 50
        cinq += 1
    while valor >= 20:
        valor = valor - 20
        vinte += 1
    while valor >= 10:
        valor = valor - 10
        dez += 1
    while valor >= 1:
        valor = valor - 1
        um += 1
    if valor == 0:
        break
print(f'Total de {cinq} cédulas de R$50')
print(f'Total de {vinte} cédulas de R$20')
print(f'Total de {dez} cedulas de R$10')
print(f'Total de {um} cédulas de R$1')
print('-*' * 20)
print('Obrigado e volte sempre!')

#solução do professor

print('-*' * 20)
print('CAIXA ELETRÔNICO')
print('-*' * 20)
valor = int(input('Qual o valor a ser sacado?R$'))
#total = valor(acho que não é necessario)
nota = 50
totalnota = 0
while True:
    if valor >= nota:
        valor -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota} cédulas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        totalnota = 0
        if total == 0:
            break
print('-*' * 20)
print('Obrigado e volte sempre!')



