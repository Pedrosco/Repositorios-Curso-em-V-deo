nome_velho = ''
nomes_list = []
idade_list = []
idade_velho = 0
contador = 0
mulher_menoridade = []
mulher_maioridade = []

for i in range(0,4):
    nome = str(input('Qual é o nome? '))
    nomes_list.append(nome)
    idade = int(input('Qual é a idade? '))
    idade_list.append(idade)
    sexo = str(input('Qual é o sexo (M OU F): ').upper)
    contador = contador + 1

    if sexo == 'M':
        if idade > idade_velho:
            idade_velho = idade
            nome_velho = nome
    if sexo == 'F':
        if idade < 20:
            mulher_menoridade.append(idade)

        

print('A idade do homem mais velho é de {} e o seu nome é {}'.format(idade_velho, nome_velho))
print(' A média das idades é de: ',sum(idade_list)/contador)
print('A soma de mulheres com menos de 20 é de:  {}'.format(len(mulher_menoridade)))
