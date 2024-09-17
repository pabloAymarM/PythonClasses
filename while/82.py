#Usuário Insira 10 valores. 1)Soma dos números positivos e quantos são negativos

numNeg = 0
numbers = 0
soma = 0

while numbers < 10:
    numbers += 1
    num = int(input('Informe um número: '))
    if num > 0:
        soma += num
    if num < 0:
        numNeg += 1
        
print(f'A soma total é {soma}.')
print(f'Há {numNeg} números negativos.')
