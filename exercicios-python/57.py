s = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while s not in 'MF':
    s =  input('Dados inválidos!\n Digite corretamente: ').strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')