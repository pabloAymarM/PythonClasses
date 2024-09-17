# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
n1 = 1
while True:
    n1 = int(input('Quer a tabuada de qual valor? '))
    if n1 > 0:
        print('-=-' *10)
        print('TABUADA DO {}:' .format(n1))
        print('{} x 0 = {}' .format(n1, n1*0))
        print('{} x 1 = {}' .format(n1, n1*1))
        print('{} x 2 = {}' .format(n1, n1*2))
        print('{} x 3 = {}' .format(n1, n1*3))
        print('{} x 4 = {}' .format(n1, n1*4))
        print('{} x 5 = {}' .format(n1, n1*5))
        print('{} x 6 = {}' .format(n1, n1*6))
        print('{} x 7 = {}' .format(n1, n1*7))
        print('{} x 8 = {}' .format(n1, n1*8))
        print('{} x 9 = {}' .format(n1, n1*9))
        print('{} x 10 = {}' .format(n1, n1*10))
        print('-=-' *10)
    if n1 < 0:
        break
print('Sinto muito, mas a nossa tabuada só aceita números positivos.')

