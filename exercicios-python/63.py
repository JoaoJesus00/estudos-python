print('--- Sequência de Fibonacci ---')
n = int(input('Digite o número de termos desejados: '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2} -> ', end = '')
while c <= n:
    t3 = t1 + t2
    print(f'{t3} -> ', end = '')
    t1 = t2
    t2 = t3
    c += 1