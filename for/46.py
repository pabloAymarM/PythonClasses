#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três a que se encontram no intervalo de 1 a 500.
soma = 0
cont = 0
for im in range(1,500,2):
    if im % 3 == 0:
        soma = soma + im
        cont = cont + 1
print('A soma dos {} valores solicidades é {}.'.format(cont,soma))
        