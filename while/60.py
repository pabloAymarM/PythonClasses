#Melhore o DESAFIO 59, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('GERADOR DE PA:')
print('-=-' * 6)
first = int(input('Primeiro termo: '))
rz = int(input('Razão da PA: '))
termo = first
cont = 1
total = 0
plus = 10
while plus != 0:
    total += plus
    while cont <= total: 
        print('{} -> ' .format(termo), end='')
        termo += rz
        cont += 1
    print('PAUSA')
    plus = int(input('Quantos termos você quer mostrar a mais? '))
print('Progessão finalizada com {} termos.' .format(total))
