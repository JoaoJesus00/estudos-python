times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol',
         'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio',
         'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco',
         'Vitória', 'Internacional', 'Ceará', 'Fortaleza',
         'Juventude', 'Sport')

print(f'Lista de times: {times}')
print(f'5 primeiros colocados: {times[0:5]}')
print(f'4 últimos colocados: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
print(f'Fluminense está na posição {times.index('Fluminense') + 1}')
