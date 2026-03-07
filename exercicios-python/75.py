num = (int(input('Digite um número: ')), int(input('Digite um número: ')),
       int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 está na {num.index(3)+1}ª posição')
else:
    print(f'O valor 3 não foi digitado')
print(f'Números pares: ', end='')
for c in num:
    if c % 2 == 0:
        print(f'{c}', end=' ')