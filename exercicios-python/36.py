casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
meses = int(input('Em quantos anos será parcelado? ')) * 12
prest = (casa / meses) + ((casa / meses) * 0.05)
print(f'Valor da prestação: R${prest:.2f}')
if prest > (salario * 0.3):
    print('Empréstimo negado, valor da parcela excede 30% do salário do comprador')
else:
    print('Empréstimo aprovado')