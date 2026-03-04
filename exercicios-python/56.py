somaidade = 0
idademaisvelho = 0
nomemaisvelho = ''
mul = 0
for c in range(1, 5):
    print(f'---- {c}° pessoa -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    somaidade += idade
    if c == 1 and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if idade > idademaisvelho and sexo == 'M':
        idademaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mul += 1

media = somaidade / 4

print(f'A média de idade desse grupo é de {media} anos')
print(f'O homem mais velho é {nomemaisvelho}, com {idademaisvelho} anos')
print(f'No grupo tem {mul} mulheres com menos de 20 anos')