from datetime import date

ano_nasc = int(input('Qual é o ano de nascimento do atleta: '))
ano_atual = date.today().year 
idade = ano_atual - ano_nasc

if idade < 9:
    print('MIRIM')
elif idade == 9 or idade < 14:
    print('INFANTIL')
elif idade == 14 or idade < 19:
    print('JUNIOR')
elif idade == 19 or idade < 20:
    print('SENIOR')
else:
    print('MASTER')