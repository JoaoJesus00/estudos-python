import random
from time import sleep
print('Vamos jogar Jokenpô')
jok = ['PEDRA', 'PAPEL', 'TESOURA']
comp = random.choice(jok)
user = input('Escolha: Pedra, Papel ou Tesoura? ').strip().upper()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 11)
print(f'Escolhi {comp} e você escolheu {user}')
if comp == user:
    print('Empatamos')
elif (comp == 'PEDRA' and user == 'PAPEL') or (comp == 'PAPEL' and user == 'TESOURA') or (comp == 'TESOURA' and user == 'PEDRA'):
    print('Perdi')
elif (user == 'PEDRA' and comp == 'PAPEL') or (user == 'PAPEL' and comp == 'TESOURA') or (user == 'TESOURA' and comp == 'PEDRA'):
    print('Eu ganhei!')
else:
    print('Digite corretamente!')