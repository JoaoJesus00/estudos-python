from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print(f'Idade: {idade}')
if idade == 18:
    print(f'Você deve se alistar esse ano!')
elif idade > 18:
    print(f'Voce passou {idade - 18} ano(s) do prazo de se alistar!')
else:
    print(f'Voce terá de se alistar em {18 - idade} ano(s)')