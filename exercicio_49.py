
numero = int(input('Qual número você quer saber a tabuada?'))

print('------------------------------------------------')
print('Tabuada do {}'.format(numero))
for i in range(0,11):
    print('{} X {} = {}'.format(numero, i, numero*i))
print('-------------------------------------------------')
    