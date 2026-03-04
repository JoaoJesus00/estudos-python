lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso!')
    while True:
        p = input('Quer continuar? [S/N]').strip().upper()
        if p in 'SN':
            break
    if p in 'N':
        break
print(lista)
print(f'{len(lista)} valores digitados')
print(f'Ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'Valor 5 está na lista na(s) posição(ões): ', end='')
    for c,i in enumerate(lista):
        if i == 5:
            print(c, end='...')
else:
    print('Valor 5 não está na lista')
