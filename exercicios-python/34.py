n = float(input('Digite o valor do salário: '))
if n > 1250:
    print(f'Aumento de 10%, salário com reajuste: R${n + (n * 10 / 100):.2f}')
else:
    print(f'Aumento de 15%, salário com reajuste: R${n + (n * 15 / 100):.2f}')