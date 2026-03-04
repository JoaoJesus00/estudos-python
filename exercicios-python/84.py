pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while True:
        p = input('Quer continuar? [S/N] ').strip().upper()
        if p in 'SN':
            break
    if p in 'N':
        break
print(f'{len(pessoas)} pessoas cadastradas')
print(f'O maior peso foi de {maior}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end='...')
print(f'\nO menor peso foi de {menor}Kg, peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end='...')