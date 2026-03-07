t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
while c <= 10:
    print(f'{t} -> ', end = '')
    t += r
    c += 1
