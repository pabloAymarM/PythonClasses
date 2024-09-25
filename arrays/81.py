# Desenvolva um programa que leia uma lista de eventos agendados para o mês e permita ao usuário adicionar novos eventos e remover eventos existentes. Exiba a lista atualizada de eventos.

print('Menu de Gerenciamento de Eventos')
escolha = 0
eventos = []

while escolha != 3:
    print('1.Adcionar um novo evento;\n2.Remover um evento;\n3.Sair.')
    escolha = int(input('Escolha uma opção (1-3): '))
    if escolha == 1:
        add = str(input('Adicione o novo evento: '))
        eventos.append(add)
    elif escolha == 2:
        remove = int(input('Qual é a posição do evento? '))
        eventos.pop(remove)
    elif escolha == 3:
        break
    print(eventos)
    
print(f'A sua lista de eventos está assim: {eventos}')