maior = homens = mulheres = 0
perfis = 1
while True:
    idade = int(input('Qual a sua idade?'))
    while idade < 1 or idade > 100:
        print('Por favor, informe corretamente.')
        idade = int(input('Qual a sua idade?'))
    if idade > 18:
        maior += 1
    sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
    while sexo not in 'FM':
        print('Por favor, informe corretamente.')
        sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print('-*' * 20)
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        print('Por favor, informe corretamente.')
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'S':
        print('-*' * 20)
        perfis += 1
    elif continuar == 'N':
        print('-*' * 20)
        break
print('Foram analisados {} perfis. Dentre eles estavam:'.format(perfis))
print('{} pessoas têm mais de 18 anos;'.format(maior))
print('{} pessoas são homens;'.format(homens))
print('E {} pessoas são mulheres e têm menos de 20 anos.'.format(mulheres))

#solução do professor

'''maior = homens = mulheres = 0
while True:
    idade = int(input('Qual a sua idade?'))
    sexo = ''
    while sexo not in 'FM':
        sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break   
print('-*' * 20)
print('{} pessoas têm mais de 18 anos;'.format(maior))
print('{} pessoas são homens;'.format(homens))
print('E {} pessoas são mulheres e têm menos de 20 anos.'.format(mulheres))'''
