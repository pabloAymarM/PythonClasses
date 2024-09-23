pessoa = ['Maria', '48', 'Rua 10']
print(pessoa)

#starting
dadosPessoais = {
    'nome:':'João',
    'Idade':23,
    'Endereço':'Avenida 4'
}

print(dadosPessoais)

#print without {}
print(dadosPessoais.keys())

#print separate without {}
print(dadosPessoais.values())

#print separate
print(dadosPessoais.items())

#dictionary with details
for chave, valor in dadosPessoais.items():
    print(f'{chave} : {valor}')
    
#add in dictionary
dadosPessoais['Peso'] = 68
print(dadosPessoais)

dadosPessoais.update({'Profissão':'Engenheiro'})
print(dadosPessoais)

#delete in dictionary
dadosPessoais.pop('Endereço')
print(dadosPessoais)

del(dadosPessoais['Endereço'])
print(dadosPessoais)