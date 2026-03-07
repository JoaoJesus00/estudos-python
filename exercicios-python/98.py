from time import sleep
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    :param i: inicio
    :param f: fim
    :param p: passo
    :return: sem retorno
    """
    print('-=' * 20)
    num = i
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} até {f} de {p} em {p}:')
    if i < f:
        while num <= f:
            sleep(0.3)
            print(num, end=' ')
            num += p
    else:
        while num >= f:
            sleep(0.3)
            print(num, end=' ')
            num -= p
    print()

contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
i = int(input('Ínicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

help(contador)