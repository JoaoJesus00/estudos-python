total = cont = maisbarato = maisdemil = menor = 0
while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        maisbarato = nome
        menor = preco
    if preco > 1000:
        maisdemil += 1
    parada = ' '
    while parada not in 'SN':
        parada = input('Deseja continuar? [S/N] ').strip().upper()
    if parada in 'N':
        break
print('Encerrado')
print(f'Total da compra: R${total:.2f}')
print(f'{maisdemil} produtos custam mais de R$1000,00')
print(f'{maisbarato} é o produto mais barato, custando R${menor:.2f}')
