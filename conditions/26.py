#Faça um programador pensar em número entre 0 e 5, peça para o usuário tentar descobrir qual foi o númeor escolhido pelo computador.
#O prrograma deverá escrever na tela se o usuário ganhou ou perdeu.
import random
n = random.randint(0,5)
n2 = int(input('Digite um número inteiro de 0 a 5: '))

print('O computador escolheu o número {}.' .format(n))
if n == n2:
    print('Você acertou!')
else:
    print('Você esoclheu o número errado.')