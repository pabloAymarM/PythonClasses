#Refaça o DESAFIO 49, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a esttrutura while.
print('GERADOR DE PA:')
print('-=-' * 6)
first = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
termo = first
cont = 1

while cont <= 10:
    print('{} -> ' .format(termo), end='')
    termo += rz
    cont += 1
print('FIM')