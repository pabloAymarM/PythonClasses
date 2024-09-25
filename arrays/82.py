#Crie um jogo em que uma lista de palavras é apresentada ao usuário, em seguida essa lista será embaralhada e não será mais mostrada ao usuário.
#O programa deverá escolher uma palavra aleatória da lista,
#exibir essa palavra
#e perguntar ao usuário em qual posição se encontra essa palavra
#o usuário terá 3 chances para acertar
#caso o usuário erre exiba uma mensagem que ele errou e diga quantas tentativas restam
#se terminar as tentativas e o usuário não acertar informe a posição
#caso acerte exiba uma mensagem de parabéns
#Em qualquer das situações, ao terminar o jogo exiba a lista embaralhada.

from random import shuffle, choice
import os
import time

animais = [ 'leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo' ]

shuffle(animais)
print(animais)
time.sleep(5)
os.system("cls")

pRandom = choice(animais)
indice = animais.index(pRandom)

while escolha != indice:
    print(f'A palavra escolhida é {pRandom}')
    print('Você tem 3 Chances!')
    escolha = int(input('Em qual posição se encontra essa palavra? (0-14)'))
    if escolha != pRandom:
        print('Ainda restam 2 Chances.')
        escolha = int(input('Em qual posição se encontra essa palavra? '))
        if escolha != pRandom:
            print('Ainda resta 1 Chance.')
            escolha = int(input('Em qual posição se encontra essa palavra? '))
            if escolha != pRandom:
                print(f'Você perdeu. A posição era {indice}')
                break
    elif escolha == indice:
        print('Você ganhou!')
        break

print(animais)