s = str(input('Qual o seu sexo?[M/F]')).upper().strip()
while s not in 'MF':
    s = str(input('Dados inválidos, por favor, tente novamente:')).upper().strip()
if s == 'M':
    print('Você declarou que é do sexo Masculino.')
elif s == 'F':
    print('Você declarou que é do sexo Feminino.')
print('Ok, Obrigada pela colaboração.')

