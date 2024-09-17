#Crie um programa que leia a data de nascimento de 7 pessoas. No final, mostre quantas pessoas não atingiram a maioridade e quantas já são maiores.
from datetime import date
yatual = date.today().year
totmaior = 0
totmenor = 0
for people in range(1,8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? ' .format(people)))
    age = yatual - nasc
    if age >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade.' .format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade.' .format(totmenor))