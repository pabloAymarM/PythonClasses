#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO". 
nome = input('Cidade: ')
nome1 = nome.split()
print('SANTO' in nome1[1])