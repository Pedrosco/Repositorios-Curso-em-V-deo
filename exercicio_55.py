
list_peso = []

for i in range(0,5):
    peso = int(input('Qual é o peso dessas pessoas? '))
    list_peso.append(peso)

list_peso = sorted(list_peso,reverse=True)
print('O maior peso é de {}'.format(list_peso[0]))
print('O menor peso é de {}'.format(list_peso[4]))
