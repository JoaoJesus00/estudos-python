lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no fim da lista')
    else:
        p = 0
        while p < len(lista):
            if n <= lista[p]:
                lista.insert(p, n)
                print(f'Valor adicionado na posição {p}')
                break
            p += 1
print(lista)