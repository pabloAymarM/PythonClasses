# criar uma lista contendo dois valores: “Cara” e “Coroa”
# Utilizando a biblioteca random e função choice
# crie um programa que simule o lançamento de uma moeda.
# exibir o resultado e armazenar esse resultado em uma outra lista.
# Pergunte ao usuário se ele deseja lançar a moeda novamente, em caso afirmativo refaça as etapas anteriores, em caso negativo, encerre exibindo a lista com todos os resultados
from random import shuffle, choice

moeda = ['cara', 'coroa']
escMoeda = 3
escolha = 1
list2 = []

while escolha != 0:
    shuffle(moeda)
    escMoeda = choice(moeda)
    print(f'Caiu {escMoeda}')
    list2.append(escMoeda)
    escolha = int(input('Deseja continuar? ([0.NÃO] [1.SIM]) '))

print(list2)