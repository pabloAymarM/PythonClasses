#Escreva um progrma que leia dois números inteiro e compare-os, mostrando na tela uma mensagem:
# O primeiro  valor é maior
# O segundo valor é maior
# Nenhum é maior, os dois são iguais

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    maior = n1
elif n2 > n1:
    maior = n2
print('O {} é maior.'.format(maior))