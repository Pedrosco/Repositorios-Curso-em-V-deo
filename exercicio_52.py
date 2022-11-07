numero = int(input('Qual seria o numero escolhido? '))


if numero == 2:
    print('É um numero primo')
elif numero % 2 == 0:
    print('O numero {} não é primo'.format(numero))
else:
    print('É um numero primo')