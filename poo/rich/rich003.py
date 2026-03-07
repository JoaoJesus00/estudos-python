from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')
tabela.add_column('Nome', style='red')
tabela.add_column('Preço', justify='center', style='blue')
tabela.add_row('Lápis', 'R$2,50')
tabela.add_row('Caneta', 'R$3,00')

print(tabela)