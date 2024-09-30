#Crie um programa que permita ao usuário criar um catálogo de livros.
#O catálogo deve ser representado por um dicionário onde as chaves são os títulos dos livros e os valores são os nomes dos autores. 
#O programa deve permitir ao usuário:
#Adicionar novos livros.
#Remover um livro do catálogo.
#Exibir o catálogo completo. No final, o programa deve mostrar quantos livros estão cadastrados no catálogo.
#O usuário poderá realizar essas operações o quanto quiser ou até escolher uma opção que termine o algoritmo

catg = {}
esc = 1

while esc != 0:
    tittle = str(input('Título do livro: '))
    autor = str(input('Nome do Autor: '))
    catg.update({tittle:autor})
    esc = int(input('Deseja continuar? ([0.NÃO] [1.SIM]) '))

print(f'O catálogo: {catg}')

esc2 = int(input('Deseja remover um livro? ([0.NÃO] [1.SIM]) '))

if esc2 == 1:
    livro = str(input('Qual livro você deseja remover? '))
    catg.pop(livro)

print(f'O catálogo: {catg}')
    