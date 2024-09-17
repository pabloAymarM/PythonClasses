#Faça um programa que leia um ano qualquer e mostre se ele é bissexto:
import calendar
ano = int(input('Digite um ano qualquer: '))
bi = calendar.isleap(ano)
if bi == True:
    print('O ano {}, é bissexto!' .format(ano))
else:
    print('O ano {}, não é bissexto!' .format(ano))