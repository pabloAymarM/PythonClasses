#Refaça o desafio 33 dos triângulos, acrescentando o recurso de mostrar que triângulo será formado:
# Equilátero: todos os lados iguais;
# Isóceles: dois lados iguais;
# Escaleno: todos os lados diferentes;

import math
a = float(input('Comprimento 1: '))
b = float(input('Comprimento 2: '))
c = float(input('Comprimento 3: ')) 

if b-c < a < b + c and a-c < b < a + c and a-b < c < a + b:
    print('Sim, é possível formar um Triângulo.')
    if a == b == c:
        print('O triângulo é Equilátero.')
    elif a == b or a == c or b == c:
        print('O triângulo é Isóceles.')
    else:
        print('O triângulo é Escaleno.')
else:
    print('Não é possível formar um triângulo.')