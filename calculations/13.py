#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
vd = dias * 60
vk = km * 0.15
total = vd + vk

print ('O total a pagar é R${:.2f}'.format(total))