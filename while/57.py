#Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior 
# [4] novos números
# [5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opc = 0
while opc != 5:
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
    opc = int(input('>>>> Qual é a sua opção? '))
    if opc == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é --- {} ---' .format(n1, n2, soma))
    elif opc == 2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} e {} é --- {} ---' .format(n1, n2, multiplicar))
    elif opc == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é --- {} ---' .format(n1, n2, maior))
    elif opc == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente.')
    sleep(1.5)
    print('=-=' * 10)
print('Fim do programa. Volte sempre!')