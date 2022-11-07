frase = str(input('Digite aqui sua frase: '))
remove_frase = frase.replace(" ","")
invert_fra = remove_frase[::-1]

if remove_frase == invert_fra:
    print('{} é um palindromo'.format(frase))
