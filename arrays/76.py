#peça 10 elementos. 
#verifique a existencia iguais a 10.
#mostrando a posição em que aparecem

lista = []
num10 = 0
num = 0
numLista = 0
posicao = []

for cont in range(1, 11):
    numero = int(input(f'Insira o {num+1}º número: '))
    lista.append(numero)
    num += 1
    if lista[numLista] == 10:
        numLista += 1
        posicao.append(numLista)

for elemento in lista:
    if elemento == 10:
        num10 += 1

print(lista)
print(f'Qtd de números 10: {num10}')
print(f'Posição: {posicao}')