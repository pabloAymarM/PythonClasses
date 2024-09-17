#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre o comprimento da hipotenusa.
"""
import math
cO = float(input('Cateto Oposto: '))
cA = float(input('Cateto Adjacente: '))
x1 = math.pow(cO,2)
x2 = math.pow(cA,2)
h = math.sqrt(x1+x2)
print('A hipotenusa desse triângulo é igual a {}' .format(h))
"""
"""
import math
cO = math.pow(float(input('Cateto Oposto: ')),2)
cA = math.pow(float(input('cateto Adjacente: ')),2)
h = math.sqrt(cO+cA)
print('A hipotenusa desse triângulo é igual {}'.format(h))
"""

cO = float(input('Cateto Oposto: '))
cA = float(input('Cateto Adjacente: '))
x1 = cO**2
x2 = cA**2
h = (x1+x2)**(1/2)

print('A hipotenusa desse triângulo é igual {}'.format(h))
