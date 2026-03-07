jogador = {}
lista = []
while True:
    jogador['Nome'] = input('Nome do jogador: ')
    partidas = int(input('Quantas partidas ele jogou? '))
    gols = []
    for i in range(0, partidas):
        gol_partida = int(input(f'Quantos gols na partida {i + 1}? '))
        gols.append(gol_partida)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    lista.append(jogador.copy())
    jogador.clear()
    while True:
        stop = input('Quer continuar?(S/N) ').strip().upper()[0]
        if stop in 'SN':
            break
        else:
            print('ERRO!')
    if stop == "N":
        break
print('-' * 60)
print('COD', end='  ')
for i in lista[0].keys():
    print(f'{i:<15}', end='')
print()
for c,j in enumerate(lista):
    print(f'{c:>3}  ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 pra parar) '))
    if dados == 999:
        break
    if dados >= len(lista):
        print(f'ERRO! Não existe jogador com código {dados}')
    else:
        for c,j in enumerate(lista):
            if c == dados:
                print(f' - Levantamento do Jogador {j['Nome']}: ')
                for c,v in enumerate(j['Gols']):
                    print(f'  Na partida {c + 1} fez {v} gols')
    print('-' * 60)
print('-' * 60)
print('Encerrado')
