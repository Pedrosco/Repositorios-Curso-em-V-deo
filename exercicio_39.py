from datetime import date

ano_nasc = int(input('Qual é o ano do seu nascimento?'))
data_atual = date.today().year
calculo = int((data_atual - ano_nasc))
anos_dif = 18 - calculo
anos_dif_cima = calculo - 18
if calculo < 18:
    print('Você ainda vai se alistar no serviço militar')
    print('Ainda faltam {} anos para você se alistar'.format(anos_dif))
elif calculo == 18:
    print('Você já está apto para se alistar')
else:
    print('Você já passou do período de alistamento')
    print('Já se passaram {} anos para você se alistar'.format(anos_dif_cima))
