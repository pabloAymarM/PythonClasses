#Crie um prgrama que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.
"""
from math import trunc
num = float(input('Digite um número real: '))
print ('O valor digitado foi {:.2f} e sua porção inteira é {}.' .format(trunc(num)))
"""
num = float(input('Digite um número real: '))
print('O valor digitado foi {:.3f} e sua porção inteira é {}.'.format(num, int(num)))