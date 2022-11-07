import random
import time

arraypc = ['Pedra', 'Papel', 'Tesoura']
rodadas = int(input('Quantas rodadas você quer jogar? : '))
marcador_pc = 0
marcador_us = 0

for i in range(rodadas):
    escolhapc = random.choice(arraypc)
    escolhaus = input(('Escolha entre Pedra, Papel ou Tesoura: '))
    tratamento_escolhaus = escolhaus.capitalize()
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')   
 
    ###Condicionais do PC e Usuário
    if escolhapc == 'Pedra' and tratamento_escolhaus == 'Tesoura':
        print('Você perdeu, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_pc = marcador_pc + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif escolhapc == 'Papel' and tratamento_escolhaus == 'Pedra':
        print('Você perdeu, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_pc = marcador_pc + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif escolhapc =='Tesoura' and tratamento_escolhaus == 'Papel':
        print('Você perdeu, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_pc = marcador_pc + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif tratamento_escolhaus == 'Pedra' and escolhapc == 'Tesoura':
        print('Você ganhou, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_us = marcador_us + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif tratamento_escolhaus == 'Papel' and escolhapc =='Pedra':
        print('Você ganhou, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_us = marcador_us + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif tratamento_escolhaus == 'Tesoura' and escolhapc == 'Papel':
        print('Você ganhou, o PC escolheu {} e você escolheu {}'.format(escolhapc, tratamento_escolhaus))
        marcador_us = marcador_us + 1
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif escolhapc =='Pedra' and tratamento_escolhaus == 'Pedra':
        print('Vocês empataram, ninguém ganha ponto')
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif escolhapc =='Papel' and tratamento_escolhaus == 'Papel':
        print('Vocês empataram, ninguém ganha ponto')
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))
    elif escolhapc == 'Tesoura' and tratamento_escolhaus == 'Tesoura':
        print('Vocês empataram, ninguém ganha ponto')
        print('PC: {} '.format(marcador_pc) + 'Você: {}'.format(marcador_us))

print('Acabou as rodadas, pontuação final: \n')
print('PC: {} '. format(marcador_pc) + 'X ' 'Você: {}'.format(marcador_us))