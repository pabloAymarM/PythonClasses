#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista diheiro/cheque: 10% de desconto;
# À vista no cartão: 5% de desocnto;
# Em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros;

prec = float(input('Digite o valor do produto: '))
pag =  int(input('Digite 1 para o pagamento á vista dinheiro/cheque\nDigite 2 para o pagamento à vista no cartão\nDigite 3 para o pagamento em até 2x no cartão\nDigite 4 para o pagamento no 3x ou  mais no cartão\n-> ')) 

if pag == 1:
    desc = prec * 0.10
    print('Você receberá um desconto de R${:.2f}'.format(desc))
    print('Você pagará somente R${:.2f}'.format(prec - desc))
elif pag == 2:
    desc = prec * 0.05
    print('Você receberá um desconto de R${:.2f}'.format(desc))
    print('Você pagará somente R${:.2f}'.format(prec - desc))
elif pag == 3:
    print('Você pagará o preço normal.')
    print('Você pagará R${:.2f} por mês'.format(prec/2))
elif pag == 4:
    vezes = int(input('Em quantas vezes?'))
    juros = prec * 0.20
    print('Você pagará com um juros de R${:.2f}')
    print('Você pagará R${:.2f} e pagará R${:.2f} por mês'.format(prec + juros, prec/vezes))