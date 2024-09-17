#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto:
print('Estamos co um desconto de 5% em todas as peças da loja. Calcule:')
v = float(input('Qual é o preço?: R$'))
cd = 0.05 * v
d = v - cd

print('O preço atual será de: R${:.2f}.\nVocê irá economizar R${:.2f}.\nMuito Obrigado!' .format(d,cd)) 


