# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)

# galera = [['João', 17], ['Gustavo', 40], ['Maria', 27]]
# # print(galera[0][1])
# # print(galera[1])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')
    
# galera = list()
# dado = list()
# totmai = totmen = 0
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:]) # : cópia de dados
#     dado.clear()
# # print(galera)
# for p in galera:
#     if p[1] >= 21:
#         print(f'{p[0]} é maior de idade.')
#         totmai += 1
#     else:
#         print(f'{p[0]} é menor de idade.')
#         totmen += 1
        
# print(f'Temos {totmai} maiores e {totmen} de idade.')

animais = ['Daniel', 'Victor', 'João']
print(type(animais))

print('-'*50)

for elementos in animais:
    print(elementos)
    
#1)
print('-'*50)
animais[0] = 'Coelho'
print(animais)

#2)
print('-'*50)
animais.append('Hélio') #add a new element in list
print(animais)

#
print('-'*50)
animais.insert(1, 'Cristian')
print(animais)

#3)
print('-'*50)
animais.pop() #delete the last element

#
print('-'*50)
animais.pop(0)
print(animais)