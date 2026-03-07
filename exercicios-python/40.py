n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2
print(f'Média: {media:.1f}')
if media < 5:
    print('Reprovado!')
elif media < 7:
    print('Recuperação!')
else:
    print('Aprovado!')