def ficha(n, g):
    if g.isnumeric():
        g = g
    else:
        g = int(0)
    if n.strip() == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gols no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Fez quantos gols? '))
ficha(n, g)