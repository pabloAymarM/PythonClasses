#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80kmm/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Velocidade: '))

if vel > 80:
    kms = float(input('Kms rodados acima da velocidade: '))
    print('Você receberá uma multa de R${:.2f}' .format(kms*7))
else:
    print('Sem problemas!')