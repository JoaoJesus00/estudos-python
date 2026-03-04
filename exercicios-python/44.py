preco = float(input('Valor da compra: '))
print("""Formas de pagamento:
1. À vista no dinheiro ou cheque: 10% de desconto
2. À vista no cartão: 5% de desconto
3. Em até 2x no cartão: sem juros
4. 3x ou mais no cartão: 20% de juros""")
escolha = int(input('Digite o número da forma de pagamento desejada: '))

if escolha == 1:
    print(f'Valor à vista no dinheiro ou cheque: R${preco - (preco * 0.1):.2f}')
elif escolha == 2:
    print(f'Valor à vista no cartão: R${preco - (preco * 0.05):.2f}')
elif escolha == 3:
    print(f'2x no cartão: 2 parcelas de R${preco / 2:.2f}')
elif escolha == 4:
    np = int(input('Digite o número de parcelas: '))
    print(f'{np}x no cartão: {np} parcelas de R${(preco + (preco * 0.2)) / np:.2f}')
else:
    print('Digite um número válido')