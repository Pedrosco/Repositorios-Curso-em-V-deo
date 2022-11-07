from tkinter import N


print('Bem vindo ao programa de cálculo')
valorprod = int(input('Digite o valor do produto: '))
print('1 - Dinheiro\n'
      '2 - Cartão à vista\n'
      '3 - Cartão em 2x\n'
      '4 - Cartão em 3x\n')
formapg = int(input('Selecione a forma de pagamento'))

if formapg == 1:
    valorprod = valorprod- (valorprod*10/100)
    print('O valor é de R$ {}'.format(valorprod))
elif formapg == 2:
    valorprod = valorprod - (valorprod*5/100)
    print('O valor é de R$ {}'.format(valorprod))
elif formapg == 3:
    valorprod = valorprod
    print('O valor é de R$ {}'.format(valorprod))
elif formapg == 4:
   juros = valorprod*20/100
   valorprod = valorprod + juros
   print('O valor com juros é de R$ {}'.format(valorprod)) 