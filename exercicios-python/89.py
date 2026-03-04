from time import sleep
notas = []
dados = []
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    notas.append(dados[:])
    dados.clear()
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-=' * 20)
print(f'{'Nº':<4}{'Nome':<10}{'Média':>8}')
print('-' * 40)
for c, d in enumerate(notas):
    print(f'{c:<4}{d[0]:<10}{(d[1] + d[2]) / 2:>8}')
print('-' * 40)
while True:
    perg = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if perg == 999:
        break
    print(f'Notas de {notas[perg][0]} são: {notas[perg][1], notas[perg][2]}')
    print('-' * 40)
print('FINALIZANDO...')
sleep(1)
print('Volte sempre!')
