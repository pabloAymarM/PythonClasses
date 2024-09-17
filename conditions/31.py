#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
x = float(input('Número 1: '))
y = float(input('Número 2: '))
z = float(input('Número 3: '))

print('Analisando os números...')
if x > y and z:
    maior = x
if y > x and z:
    maior = y
if z > x and y:
    maior = z
if x < y and z:
    menor = x
if y < x and z:
    menor = y
if z < x and y:
    menor = z

print('O maior número é: {:.0f}' .format(maior))
print('O menor número é: {:.0f}' .format(menor))