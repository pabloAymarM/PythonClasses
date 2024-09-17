#Crie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atigindo:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RRECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2

if media < 5:
    print('O aluno está reprovado.')
elif 5 <= media <=6.9:
    print('O aluno está de recuperação.')
elif media >= 7:
    print('O aluno está aprovado.')
print('A média do aluno é igual a {:.1f}'.format(media))