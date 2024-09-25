#crie duas listas com números pedidos para o usuário
#encontre a interseção das listas e adicione uma nova lista
#exiba a nova lista

list1 = []
list2 = []
list3 = []

for cont in range(5):
    n1 = int(input(f'Informe o número para lista 1: '))
    list1.append(n1)
    n2 = int(input(f'Informe o número para lista 2: '))
    list2.append(n2)
    
    if list1[cont] in list2:
        list3.append(list1[cont])
        cont += 1
        
print(list3)