#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
print('Economize! Descubra a quantidade exata de tinta que você deve usar:')
c = float(input('Qual é o comprimento da parede? '))
l = float(input('Qual é a largura da parede? '))

m = c*l
li = m / 2

print('Você precisará de somente: {}' .format(li))

