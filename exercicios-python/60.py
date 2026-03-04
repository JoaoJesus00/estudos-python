n = int(input('Digite um número para saber o fatorial: '))
c = n
while c != 1:
    print(f'{c} x ', end = '')
    c -= 1
    n *= c
print(f'1 = {n}')
