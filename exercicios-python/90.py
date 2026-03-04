aluno = {}
aluno['Nome'] =  input('Nome: ')
aluno['Media'] = float(input(f'Média do aluno {aluno["Nome"]}: '))
if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Aprovado'
print('-=' * 20)
for v, k in aluno.items():
    print(f'- {v} : {k}')
