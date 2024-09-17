#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input('Digite o ângulo que deseja: '))

sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tg = math.tan(math.radians(a))

print('Aqui temos todas as informações do ângulo: \nsen: {:.2f} \ncos: {:.2f} \ntg: {:.2f}'.format(sen,cos,tg))
