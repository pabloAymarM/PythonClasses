#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura em ¹C: '))

f = (c *9/5) + 32

print('A temperatura de {:.2f}¹C corresponde a {:.2f}¹F!'.format(c,f))