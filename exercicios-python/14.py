km = float(input('Quantos km foram percorridos? '))
dias = int(input('Foi alugado por quantos dias? '))
valor = (km * 0.15) + (dias * 60)
print(f'Valor a pagar: R${valor:.2f}')