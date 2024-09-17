#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
#Ex: Ana Maria de Sousa
#primeiro: Ana;
#segundo: Sousa;

nome = input('Digite seu nome: ')
nome1 = nome.split()
print('Primeiro nome: {};' .format(nome1[0]))
print('Segundo nome: {}.' .format(nome1[-1]))
