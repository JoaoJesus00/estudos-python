from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
print(f'Idade até final de 2025: {idade} anos')
if idade <= 9:
    print('Atleta mirim')
elif idade <= 14:
    print('Atleta infantil')
elif idade <= 19:
    print('Atleta junior')
elif idade <= 25:
    print('Atleta senior')
else:
    print('Atleta master')