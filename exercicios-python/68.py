from random import randint
print('      ---- Par ou ímpar ----')
total = 0
while True:
    print('-' * 40)
    comp = randint(0, 10)
    user = int(input('Digite um valor de 0 à 10: '))
    soma = comp + user
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = input('Par ou ímpar? [P/I] ').strip().upper()[0]
    print('-' * 40)
    if soma % 2 == 0:
        resul = 'P'
        print(f'Você jogou {user} e o computador jogou {comp}, deu PAR!')
    else:
        resul = 'I'
        print(f'Você jogou {user} e o computador jogou {comp}, deu ÍMPAR!')
    if escolha != resul:
        break
    total += 1
    print('-' * 40)
    print('Você venceu')
print('' * 40)
print(f'GAME OVER. Você venceu {total} vezes!')