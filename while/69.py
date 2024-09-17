#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
print('=' *30)
print('{:^30}' .format('BANCO CEV'))
print('=' *30)
money = int(input('Que valor você quer sacar? R$'))
total = money
ced = 50
totced = 0 
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('=' *30)
print('Volte sempre ao BANCO CEV!')