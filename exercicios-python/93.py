aprov = {}
aprov['Nome'] = input('Nome do jogador: ')
partidas = int(input('Quantas partidas ele jogou? '))
gols = []
for i in range(0, partidas):
    gol_partida = int(input(f'Quantos gols na partida {i + 1}? '))
    gols.append(gol_partida)
aprov['Gols'] = gols[:]
aprov['Total'] = sum(gols)
print('-=' * 20)
print(aprov)
print('-=' * 20)
for k, v in aprov.items():
    print(f'{k}: {v}')
print('-=' * 20)
print(f'O jogador {aprov['Nome']} jogou {partidas} partidas')
for c,v in enumerate(aprov['Gols']):
    print(f'    => Na partida {c + 1}, fez {v} gols')
print(f'O total foi de {aprov['Total']} gols.')