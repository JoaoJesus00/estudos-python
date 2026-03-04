from random import randint
from time import sleep
mega = []
jogo = []
cont = 0
print('-' * 30)
print('     JOGO DA MEGA-SENA')
print('-' * 30)
quant = int(input('Digite a quantidade de jogos: '))
print(f'Sorteando {quant} jogos...')
sleep(0.7)
while cont < quant:
    cont2 = 0
    while cont2 <= 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont2 += 1
    mega.append(jogo[:])
    jogo.clear()
    cont += 1
for i,j in enumerate(mega):
    print(f'Jogo {i + 1}: {sorted(j)}')
    sleep(0.7)