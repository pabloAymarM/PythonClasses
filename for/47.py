#Refaça o desafio 07, mostrando a tabuada de um núemro que o usuário escolher, só que agora usando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))
for num in range(1,11):
    print('{} x {} = {}'.format(n, num, n*num))