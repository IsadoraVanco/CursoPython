alt = float(input('Qual a sua altura? (m)'))
peso = float(input('Qual o seu peso? (kg)'))
imc = peso / (alt ** 2)
print('Seu resultado deu {:.2f}'.format(imc))
if imc < 18.5:
    print('->Abaixo do peso')
elif imc >= 18.5:
    print('->Peso ideal')
elif imc >= 25:
    print('->Sobrepeso')
elif imc >= 30:
    print('->Obesidade')
elif imc >= 40:
    print('->Obesidade mórbida')
