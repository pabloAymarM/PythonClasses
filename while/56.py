#Melhore o DESAFIO 26 onde o computador vai "pensar" em número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
# EU:
import random
pc = random.randint(0, 10)
us = int(input('Tente adivinhar o número: [0 a 10] '))

while pc != us:
    us = int(input('--- ERROR ---\nTente novamente: '))
print('Parabéns, você acertou! O número escolhido foi {}.' .format(pc))
"""
#Guanabara:
from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10 ')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!' .format(palpites))