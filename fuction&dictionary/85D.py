#Desenvolva um programa que crie um dicionário onde as chaves são os nomes dos alunos e os valores são suas respectivas notas.
#O programa deve permitir ao usuário adicionar novas entradas de alunos e suas notas.
#Em seguida, o programa deve calcular a média da turma e exibir quais alunos tiveram notas acima dessa média.

lAlunos = {}
list = []
cont = 0
soma = 0
esc = 1
somAlunos = 0

while esc != 0:
    cont += 1
    aluno = str(input(f'Aluno 0{cont}: '))
    nota = str(input(f'Nota 0{cont}: '))
    lAlunos.update({aluno:nota})
    soma += lAlunos.values()
    esc = int(input('Deseja continuar? ([0.NÃO] [1.SIM]) '))
    
media = soma / cont

for chave, valor in lAlunos.items():
    if valor > media:
        list.append(chave)

print('A média da turma é {media}, e os alunos que acima da média são {list}')