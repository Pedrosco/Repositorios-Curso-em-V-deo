n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a nota do aluno: '))
media = (n1+n2)/2

if media < 5.0:
    print('REPROVADO !')
elif media == 5.0 or media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO')

print(media)