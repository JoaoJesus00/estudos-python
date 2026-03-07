def area(l, c):
    print(f'A área de um terreno {l}X{c} é de {l * c}m².')


print('Controle de terrenos')
print('-' * 30)
larg = float(input('Largura (m): ' ))
comp = float(input('Comprimento (m): '))
area(larg, comp)