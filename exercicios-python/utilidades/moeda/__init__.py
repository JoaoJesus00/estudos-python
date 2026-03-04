def linha():
    print('-' * 40)

def metade(n, f=False):
    r = n / 2
    return r if f is False else moeda(r)


def dobro(n, f=False):
    r = n * 2
    return r if f is False else moeda(r)


def aumentar(n, p, f=False):
    r = n + (n * (p / 100))
    return r if f is False else moeda(r)


def reduzir(n, p, f=False):
    r = n - (n * (p / 100))
    return r if f is False else moeda(r)


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(p, a, r):
    linha()
    print(f'RESUMO DO VALOR'.center(40))
    linha()
    print(f'Preço analisado: \t{moeda(p):>20}')
    print(f'Dobro do preço: \t{dobro(p, True):>20}')
    print(f'Metade do preço: \t{metade(p, True):>20}')
    print(f'{a}% de aumento: \t{aumentar(p, a, True):>20}')
    print(f'{r}% de redução: \t{reduzir(p, r, True):>20}')
    linha()