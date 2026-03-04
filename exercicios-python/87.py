matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
coluna3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição {l, c}: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        coluna3 += matriz[l][2]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'Soma dos números pares = {pares}')
print(f'Soma dos valores da coluna 3 = {coluna3}')
print(f'Maior valor da segunda linha = {max(matriz[1])}')