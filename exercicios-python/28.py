from random import randint
comp = randint(0, 5)
num = int(input('Descubra o número de 0 a 5 que estou pensando: '))
if num == comp:
    print('Você acertou!')
else:
    print(f'Você errou, era o número {comp}')