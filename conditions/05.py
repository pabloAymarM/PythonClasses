#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média:
math = float(input('Matemática: '))
port = float(input('Português: '))
s = math + port
m = s/2

if m >= 7:
    print(' Sua média é: {}.\n VOCÊ PASSOU! :)' .format(m))
else:
    print (' Sua média é: {}. \n VOCÊ NÃO PASSOU, INFELIZMENTE. :(' .format(m))
    

  