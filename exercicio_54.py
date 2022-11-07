from datetime import date

data_atual = int(date.today().year) 
array_maioridade = []
array_menoridade = []

for i in range(0,7):
    ano_nasc = int(input('Digite o ano de nascimento dessas pessoas'))
    calculo_id = data_atual - ano_nasc
    if calculo_id >= 21:
        array_maioridade.append(calculo_id)
    else:
        array_menoridade.append(calculo_id)

print('{} pessoas estão na maioridade'.format(len(array_maioridade)))
print('{} pessoas ainda estão na menoridade'.format(len(array_menoridade)))

