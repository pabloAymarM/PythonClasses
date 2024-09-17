#Crie um programa que leia o número e mostre na tela se ele é par ou ímpar.
n = float(input('Digite um número: '))
resto = n % 2

if resto == 0:
    print('Número é par.')
else:
    print('Número é ímpar.')