from random import randint
comp = randint(0, 10)
user = int(input('Adivinhe o número de 0 à 10 que estou pensando: '))
tentativas = 1
while user != comp:
    tentativas += 1
    if user > comp:
        user = int(input('Menos, tente de novo: '))
    else:
        user = int(input('Mais, tente de novo: '))
print(f'Isso, número {comp}, você acertou em {tentativas} tentativas!')