from random import randint
from time import sleep
def sorteia(lst):
    print('Sorteando:')
    for i in range(0, 5):
        sleep(0.3)
        lst.append(randint(0, 10))
        print(lst[i], end=' ')
    print()

def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 == 0:
            soma += v
    sleep(0.3)
    print(f'Soma dos valores pares = {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)