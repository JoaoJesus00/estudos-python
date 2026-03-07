def voto(n):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade > 65 or (18 > idade >= 16):
        print(f'Com {idade} anos: Voto opcional!')
    elif idade > 18:
        print(f'Com {idade} anos: Voto obrigatório!')
    else:
        print(f'Com {idade} anos: Voto negado!')


ano = int(input('Ano de nascimento: '))
voto(ano)