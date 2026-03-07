num = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Não adicionado, valor repetido!')
    while True:
        p = input('Quer continuar? [S/N] ').strip().upper()
        if p in 'SN':
            break
    if p in 'N':
        break
print(sorted(num))