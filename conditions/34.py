#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Digite o valor da casa: R$'))
sal = float(input('DIgite seu salário: R$'))
meses = int(input('Em quantos meses você vai pagar? '))

val = casa/meses
if val >= 0.3*sal:
    print('Você não pode comprar essa casa!')
else:
    print('Ok, você pode continuar.')
