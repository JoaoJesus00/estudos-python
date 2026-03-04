from rich.panel import Panel
from rich import print
from rich import inspect

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = str(f'R${preço:.2f}')

    def etiqueta(self):
        conteudo = f'{self.nome.center(30)}'
        conteudo += '-' * 30
        conteudo += f'{self.preço.center(30, '.')}'
        print(Panel(conteudo, title='Produto', width=34))


p1 = Produto('Iphone 17 Pro Max', 10000)
p1.etiqueta()

p2 = Produto('Mouse', 100)
p2.etiqueta()