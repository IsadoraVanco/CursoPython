num = soma = quant = 0
while True:
    num = int(input('Digite um número [999 para parar]:'))
    if num == 999:
        break
    soma += num
    quant += 1
print(f'Você digitou {quant} números, e a soma entre eles foi de {soma}.')
