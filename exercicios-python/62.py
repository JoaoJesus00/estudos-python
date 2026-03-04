t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(f'{t} -> ',end = '')
        t += r
        c += 1
    mais = int(input('Mais quantos termos? '))
print(f'Finalizado com {total} termos')