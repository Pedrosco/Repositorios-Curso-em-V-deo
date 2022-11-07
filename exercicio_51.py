termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
ultimo = 0
numero = []

ultimo = termo + (11-1)*razao

for i in range(termo,ultimo,razao):
    numero.append(i)
print(numero)