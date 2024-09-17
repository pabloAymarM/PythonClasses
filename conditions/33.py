#Desenvolva um programa que leia o comprimento de três reetas e diga ao usuário se elas podem ou não formar um triângulo.
import math
a = float(input('Comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: ')) 

if b-c < a < b + c and a-c < b < a + c and a-b < c < a + b:
    print('Sim, é possível!')
    if a == b == c:
        print('O triângulo é equilátero.')
else:
    print('Não é possível!')