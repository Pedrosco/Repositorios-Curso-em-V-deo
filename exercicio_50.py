s = 0

for i in range(0,6):
    numero = int(input('Qual é o número que você deseja? '))
    if numero % 2 == 0:
        s += numero
print('A soma dos numeros pares é de {}'.format(s))