#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual base de conversão:
# 1 - binário;
# 2 - octal;
# 4 - hexadecimal.

num = int(input('Digite um número: ')) 
base = int(input('Digite [1] para transformar em binário; \nDigite [2] para transformar em octal; \nDigite [3] para trasnformar em hexadecimal.\n'))

if base == 1:
    conversao = bin(num)[2:]
elif base == 2:
    conversao = oct(num)[2:]
elif base == 3:
    conversao = hex(num)[2:]
else:
    print('Número inválido!')
print('O número {} convertido para a base {} é {}' .format(num,base,conversao))