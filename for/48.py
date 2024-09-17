#Desenvolva um programa que leia seis números interios e mostre a soma somente daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for n in range(1,7):
    ns = int(input('Número 0{}: '.format(n)))
    if ns % 2 == 0:
        soma += ns
        cont += 1
print('A soma dos números pares é igual a {}'.format(soma))
