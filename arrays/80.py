#Escreva um programa que solicite as notas de um aluno e armazene em uma lista (será preciso digitar zero para terminar), após isso, determine quantos alunos ficaram com a nota acima da média (no caso seria 7).
#Exiba a quantidade de alunos que tiveram notas acima da média da turma.

nota = 1
nAlunosMedia = 0
list = []

print('===== DIGITE [0] PARA PARAR =====')
while nota != 0:
    nota = float(input('Informe a nota do aluno: '))
    list.append(nota)

for nAlunos in list:
    if nAlunos > 7:
        nAlunosMedia += 1

print(nAlunosMedia)