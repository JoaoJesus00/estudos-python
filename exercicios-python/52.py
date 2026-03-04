n = int(input('Digite um número inteiro para saber se é primo: '))
d = 0
for c in range(2, n):
    if n % c == 0:
        d += c
if d == 0:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')