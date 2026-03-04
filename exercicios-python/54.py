from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    idade = atual - int(input(f'Digite o ano de nascimento da pessoa {c}: '))
    if idade < 18:
        menor += 1
    else:
        maior += 1
print(f'Maiores = {maior}')
print(f'Menores = {menor}')