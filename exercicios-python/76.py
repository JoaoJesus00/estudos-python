lista = ('Lápis', 1.50, 'Caderno', 8, 'Borracha', 2, 'Régua', 7,
         'Apontador', 3, 'Caneta', 2, 'Tesoura', 5, 'Mochila', 45)
print('=' * 30)
print(f'{"LISTAGEM DE PRODUTOS":^30}')
print('=' * 30)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20}', end='')
    else:
        print(f'R$ {lista[c]:.2f}')