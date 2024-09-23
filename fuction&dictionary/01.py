#Crie um dicionário que represente um grupo de pessoas e seus respectivos telefones.                                                                                       As chaves devem ser os nomes das pessoas e os valores devem ser os seus números de telefone. Ao final exiba o dicionário.

n = 1
tel = ' '
nome = ' '

dadosPessoais = {
    nome : tel
}

while n != 0:
    nome = input('Inofrme o seu nome: ')
    tel = input('Informe o seu telefone: ')
    dadosPessoais[nome] = tel
    
    n = input('Deseja continuar? [S/N] ')
    if n == 'n' or n == 'N':
        break
    
dadosPessoais.pop(' ')

print(dadosPessoais)