#Desenolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média da idade do grupo;
# Qual é o nome do mais velho;
# Quantas mulheres tem menos de 20 anos;
soma_age = 0
media_idade = 0
maior_h = 0
nome_velho = ''
tot_mulher20 = 0
for people in range(1,5):
    print('----- {}ª PESSOA -----' .format(people))
    nome = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_age += age
    if people == 1 and sexo in 'Mm':
        maior_h = age
        nome_velho = nome
    if sexo in 'Mm' and age > maior_h:
        maior_h = age
        nome_velho = nome
    if sexo in 'Ff' and age < 20:
        tot_mulher20 += 1
media_idade = soma_age / 4

print('A média de idade do grupo é de {} anos.' .format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.' .format(maior_h, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(tot_mulher20))

'''
for p in range(1,5):
    print('PESSOA 0{} '.format(p))
    ps = input('Digite seu nome: ')
    ids = int(input('Digite sua idade: '))
    itens = ['MASCULINO', 'FEMININO']
    print('SEXO: \n[0]MASCULINO \n[1]FEMININO')
    sx = int(input('[0] ou [1]: '))
    print('{}'.format(itens[sx]))
print('PESSOA 0{}: \nNome: {}; \nIdade: {}; \nSexo: {}.'.format(p, ps, ids, itens[sx]))
print('PESSOA 0{}: \nNome: {}; \nIdade: {}; \nSexo: {}.'.format(p, ps, ids, itens[sx]))
print('PESSOA 0{}: \nNome: {}; \nIdade: {}; \nSexo: {}.'.format(p, ps, ids, itens[sx]))
print('PESSOA 0{}: \nNome: {}; \nIdade: {}; \nSexo: {}.'.format(p, ps, ids, itens[sx]))
'''