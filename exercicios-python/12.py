preco = float(input('Digite o valor do produto: '))
novo_preco =  preco - (preco * 5 / 100)
print(f'Esse produto com 5% de desconto sai por R${novo_preco:.2f}')