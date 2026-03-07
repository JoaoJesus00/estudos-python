lista = []
pessoa = {}
soma_idade = 0
while True:
    pessoa['Nome'] = input('Nome: ')
    while True:
        pessoa['Sexo'] = input('Sexo [M/F]: ').strip().upper()
        if pessoa['Sexo'] in "MF":
            break
        else:
            print('ERRO! Responda apenas com M ou F')
    pessoa['Idade'] = int(input('Idade: '))
    soma_idade += pessoa['Idade']
    while True:
        stop = input('Quer continuar? [S/N]').strip().upper()
        if stop in 'SN':
            break
        else:
            print('Erro! Responda apenas com S ou N')
    lista.append(pessoa.copy())
    pessoa.clear()
    if stop == 'N':
        break
media = soma_idade / len(lista)
print('-=' * 20)
print(f' - Ao todo temos {len(lista)} pessoas cadastradas')
print(f' - A média de idade é de {media:.2f} anos')
print(' - Mulheres cadastradas: ')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'  {p['Nome']}')
print('- Pessoas acima da média: ')
for p in lista:
    if p['Idade'] > media:
        for k,v in p.items():
            print(f'{k} = {v};', end=' ')
print('-=' * 20)
print('Encerrado')