numero_1 = int(input('Qual é o valor do primeiro número? '))
numero_2 = int(input('Qual é o valor do segundo número? '))


if numero_1 > numero_2:
    print('O maior número é o {}'.format(numero_1))
    print('O menor número é o {}'.format(numero_2))
elif numero_2 > numero_1:
      print('O maior número é o {}'.format(numero_2))
      print('O menor número é o {}'.format(numero_1))
else:
    print('Os dois números são iguais;')