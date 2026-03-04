maioridade = homens = mulheres = 0
while True:
    idade = int(input(f'Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input(f'Sexo: [M/F] ').strip().upper()
    if idade >= 18:
        maioridade += 1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    parada = ' '
    while parada not in 'SN':
       parada = input('Deseja continuar? [S/N] ').strip().upper()
    print('-' * 30)
    if parada not in 'S':
        break
print('-' * 30)
print('Encerrado!')
print(f'{maioridade} pessoas com mais de 18 anos.')
print(f'{homens} homens.')
print(f'{mulheres} mulheres com menos de 20 anos.')
