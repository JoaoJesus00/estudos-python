from random import randint
num = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print('Números sorteados: ', end='')
for c in num:
    print(f'{c} ', end='')
print(f'\nMaior: {max(num)}, Menor: {min(num)}')