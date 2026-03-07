lista = []
par = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    while True:
        p = input('Quer continuar? [S/N] ').strip().upper()
        if p in 'SN':
            break
    if p in 'N':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Números digitados: {lista}')
print(f'Pares: {par}')
print(f'Ímpares: {impar}')