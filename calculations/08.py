#Crie um programa que leia o quanto de dinheiro que uma pessoa tem na carteira e mostre quantos dólares ela pode comprar:
#Considere: US$: 1,00 == R$ 5,25

print('Descubra quantos dólares você pode comprar.')
r = float(input('Quantos reais você tem na sua carrteira? R$'))

d = r / 5.25
print('Com {} você pode comprar {} dólares.'.format(r,d)) 