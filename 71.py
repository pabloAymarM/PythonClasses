#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = 'América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Internacional', 'Palmeiras', 'Chapecoense', 'RB Bragantino', 'Santos', 'São Paulo', 'Vasco'
print('=' *30)
print(f'Os 5 primeiros colocados: {times[0:5]}.')
print('=' *30)
print(f'O Z4: {times[-4:]}.')
print('=' *30)
print(sorted(times))
print('=' *30)
print(times.index('Chapecoense'))