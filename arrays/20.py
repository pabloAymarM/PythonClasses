#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas;
# - O nome com todas minúsculas;
# - Quantas letras ao todo sem considerar os espaços;
# - Quantas letras o primeiro nome;

nome = input('Digite seu nome completo: ')

print('Seu nome em maiúsculo é {}' .format(nome.upper()))
print('Seu nome em minúsculo é {}' .format(nome.lower()))
espaco = nome.replace(" ", "")
print('Seu nome ao todo tem {} letras' .format(len(espaco)))
lista = nome.split()
nome1 = lista[0]
print('Seu primeiro nome é {} e ele tem {} letras' .format(nome1, len(lista[0])))