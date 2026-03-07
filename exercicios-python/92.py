#Carteira de trabalho e aposentadoria
from datetime import datetime
pessoa = {}
pessoa['Nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = datetime.now().year - nasc
pessoa['CT'] = int(input('Carteira de trabalho (0 se não possui): '))
if pessoa['CT'] == 0:
    print('-=' * 20)
    for k, v in pessoa.items():
        print(f'{k}: {v}')
else:
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] + 35) - nasc
    print('-=' * 20)
    for k, v in pessoa.items():
        print(f'{k}: {v}')