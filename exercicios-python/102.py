def fatorial(n, show=False):
    """
    Função para calcular fatorial
    :param n: número a ser fatorado
    :param show: mostrar ou não o cálculo
    :return: retorna o resultado do cálculo
    """
    v = 1
    for i in range(n, 0, -1):
        print(i, end=' ')
        if i > 1:
            print('X', end=' ')
        else:
            print('=', end=' ')
        v *= i
    return v

print(fatorial(5, True))
help(fatorial)