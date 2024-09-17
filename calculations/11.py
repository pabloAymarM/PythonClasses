#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de desconto:
print('Descubra qual será o seu novo salário:')
st = float(input('Digite o seu salário atual: R$'))

d = 0.15 * st
sn = st + d

print('Você recebeu um aumento de R${:.2f} e o seu novo salário é: R${:.2f}.'.format(d,sn)) 
