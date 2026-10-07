#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Santos', 'Botafogo', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama', 'Paraná', 'Vitória', 'América-MG', 'Sport')

print(f'os 5 primeiros colocados são: {times[0:5]}')
print('Os 4 ultimos colocados são: {times[-4:]}')
print(sorted(times))
print(f'o Chapecoense esta na posição {times.index("Chapecoense")+1}')
