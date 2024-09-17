#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até tr um valor correto.
sx = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sx not in 'MF':
    sx = str(input('Dados inválidos. Por favor, informe o seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo {}, registado com sucesso.' .format(sx))