leve = 0
pesado = 0
for c in range(1,6):
    medida = float(input('Qual o peso da {}ª pessoa?'.format(c)))
    if c == 1:
       leve = medida = pesado
    else :
          if medida > pesado:
            pesado = medida
          elif medida < leve:
            leve = medida
print('A pessoa mais pesada tem {}Kg'.format(pesado))
print('E a pessoa mais leve tem {}Kg'.format(leve))
