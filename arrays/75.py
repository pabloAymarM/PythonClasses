#peça 7 números. 
#insira em uma lista. 
#calcule Todos.
#mostre a quantidade de números pares.

lista = []
soma = 0
numImp = 0

for cont in range(8):
    numero = int(input('Insira um número: '))
    lista.append(numero)
    soma += numero
    
    if numero % 2 != 0:
        numImp += 1    
        
print(f'Soma: {soma}')
print(f'Qtd de Impares: {numImp}')


