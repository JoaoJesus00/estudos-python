km = int(input('Qual a distância em km? '))
if km > 200:
    print(f'Valor da passagem: R${km * 0.45:.2f}')
else:
    print(f'Valor da passagem: R${km * 0.50:.2f}')