from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
rank = []
print('Valores sorteados: ')
sleep(0.5)
for k, v in jogadores.items():
    print(f'{k} = {v}')
    sleep(0.5)
print('-=' * 20)
print('Ranking dos jogadores: ')
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for c, v in enumerate(rank):
    print(f'{c+1}º Lugar: {v[0]} com {v[1]} pontos')
