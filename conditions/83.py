#Crie um programa que faça o commputador jogar jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? ')) 
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=-'*10)
print('Computador escolheu {}.'.format(itens[comp]))
print('Você escolheu {}.'.format(itens[jogador]))
print('-=-'*10)

if comp == 0:
    if jogador == 0:
        print('\033[3;33mEMPATE\033[m')
    elif jogador ==  1:
        print('\033[3;32;40mJOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[3;31;40mJOGADOR PERDEU!\033[m')
    else: 
        print('JOGADA INVÁLIDA!') 
elif comp == 1:
    if jogador == 0:
        print('\033[3;31;40mJOGADOR PERDEU!\033[m')
    elif jogador ==  1:
        print('\033[3;33mEMPATE\033[m')
    elif jogador == 2:
        print('\033[3;32;40mJOGADOR VENCEU!\033[m')
    else: 
        print('JOGADA INVÁLIDA')   
elif comp == 2:
    if jogador == 0:
        print('\033[3;32;40mJOGADOR VENCEU!\033[m')
    elif jogador ==  1:
        print('\033[3;31;40mJOGADOR PERDEU!\033[m')
    elif jogador == 2:
        print('\033[3;33mEMPATE\033[m')
    else: 
        print('JOGADA INVÁLIDA')