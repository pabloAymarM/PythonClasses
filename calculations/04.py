#Crie um algoritmo que leia um número e mostre seu dobro, triplo e raíz quadrada:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print(' Obrigado! Assim conseguimos calcular:\n o dobro: {};\n o triplo: {};\n a raíz quad: {:.2f};'.format(d,t,r))